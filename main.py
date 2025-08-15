# THE PURPOSE OF THIS FILE (main.py) IS PURELY FOR UI-BUILDING AND DOES NOT HAVE ANY LOGIC.
# THIS FILE CREATES A WEB LANDING PAGE AND HAVE EVERY UI ELEMENTS.
# THE LOGIC IS HANDLED IN analyzer.py FILE.

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from analyzer import StockSentimentAnalyzer
import pandas as pd

def main():
    # 1. CONFIGURATION
    st.set_page_config(
        page_title="Stock Sentiment Analyzer",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.title("US Stock Sentiment Analyzer")
    st.markdown("Analyzing sentiment of US stock-related news to make informed decisions.")

    # 2. INITIALIZATION
    analyzer = StockSentimentAnalyzer()

    # 3. SIDEBAR CONFIGURATION
    st.sidebar.header("Configurations")
    symbol = st.sidebar.text_input(
        "Stock Symbol", value="TSLA",
        help="Enter stock ticker (eg. TSLA, AAPL, INFY.NS)"
    ).upper()
    period = st.sidebar.selectbox("Period", ["1mo", "3mo", "6mo", "1y", "2y"], index=0)
    news_count = st.sidebar.slider("Number of News Headlines", 50, 1000, 100,)

    # 4. EVENT HANDLER
    if st.sidebar.button("Analyze", type="primary"):
        tab1, tab2, tab3 = st.tabs(["Overview", "News Analysis", "Stock Performance"])
        with st.spinner("Fetching and analyzing data..."):
            stock_data = analyzer.get_stock_data(symbol, period)
            news_df = analyzer.get_news(symbol, news_count)

            if stock_data is not None and not news_df.empty:
                analyzed_news = analyzer.analyze_and_get_sentiments(news_df)
                st.success("Analysis complete! Explore the tabs below.")

                # TAB 1: Overview
                with tab1:
                    st.header(f"Analysis Overview for ${symbol}")

                    average_score = round(analyzed_news['score_vader'].mean(), 2)
                    scaled_score = round((average_score + 1) * 5, 1)

                    sentiment_label = "Neutral"
                    if average_score > 0.05:
                        sentiment_label = "Positive"
                    elif average_score < -0.05:
                        sentiment_label = "Negative"

                    total_news = len(analyzed_news)
                    positive_news = len(analyzed_news[analyzed_news['sentiment_vader'] == 'Positive'])
                    negative_news = len(analyzed_news[analyzed_news['sentiment_vader'] == 'Negative'])

                    positive_pct = round((positive_news / total_news) * 100, 1) if total_news > 0 else 0
                    negative_pct = round((negative_news / total_news) * 100, 1) if total_news > 0 else 0

                    start_price = stock_data['Close'].iloc[0]
                    end_price = stock_data['Close'].iloc[-1]
                    price_change = round((end_price - start_price) / start_price * 100, 2)

                    col1, col2, col3, col4 = st.columns(4)
                    col1.metric("Overall Sentiment Score", f"{scaled_score}/10", delta=sentiment_label)
                    col2.metric("Price Change", f"{price_change}%", delta=f"from {start_price} to {end_price}")
                    col3.metric("Positive News", f"{positive_news} ({positive_pct}%)")
                    col4.metric("Negative News", f"{negative_news} ({negative_pct}%)")

                # TAB 2: News Sentiment Analysis
                with tab2:
                    st.header("News Sentiment Analysis")
                    analyzed_news['created_at'] = pd.to_datetime(analyzed_news['created_at'])

                    daily_sentiment = analyzed_news.resample('D', on='created_at')['score_vader'].mean().ffill()

                    st.subheader("Daily Sentiment Trend")
                    fig = px.line(
                        daily_sentiment,
                        x=daily_sentiment.index,
                        y='score_vader',
                        title='Sentiment Score Over Time',
                        labels={'created_at': 'Date', 'score_vader': 'Average VADER Score'}
                    )
                    fig.update_layout(showlegend=False)
                    st.plotly_chart(fig, use_container_width=True)

                # TAB 3: Stock Performance
                with tab3:
                    st.header("Detailed Stock Performance")
                    fig = go.Figure()

                    fig.add_trace(go.Candlestick(
                        x=stock_data.index,
                        open=stock_data['Open'],
                        high=stock_data['High'],
                        low=stock_data['Low'],
                        close=stock_data['Close'],
                        name='Price'
                    ))

                    fig.add_trace(go.Bar(
                        x=stock_data.index,
                        y=stock_data['Volume'],
                        name='Volume',
                        yaxis='y2'
                    ))

                    fig.update_layout(
                        title=f'{symbol} Price and Trading Volume',
                        yaxis_title='Stock Price (USD)',
                        yaxis2=dict(
                            title='Volume',
                            overlaying='y',
                            side='right'
                        ),
                        xaxis_rangeslider_visible=False
                    )

                    st.plotly_chart(fig, use_container_width=True)

            else:
                st.error("Could not fetch data. Please check the stock symbol and try again.")
    else:
        st.info("Configure your analysis in the sidebar and click 'Analyze'.")

if __name__ == "__main__":
    main()
