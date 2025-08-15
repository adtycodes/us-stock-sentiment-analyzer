import pandas as pd
import numpy as np
import yfinance as yf
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import datetime, timedelta
import re
from news_scraper import NewsDataScraper

class StockSentimentAnalyzer:
    def __init__(self):
        self.vader_analyzer = SentimentIntensityAnalyzer()

    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        text = re.sub(r'[\@\#]', '', text)
        text = re.sub(r'[^A-Za-z0-9 ]+', '', text)
        return text.strip()
        
    def get_stock_data(self, symbol, period="1mo"):
        try:
            stock = yf.Ticker(symbol)
            data = stock.history(period=period)
            if data.empty:
                print(f"Warning: No data found for {symbol}.")
                return None
            return data
        except Exception as e:
            print(f"Error fetching stock data for {symbol}: {str(e)}")
            return None
        
    def get_news(self, symbol, count=100):
        scraper = NewsDataScraper()
        news_df = scraper.fetch_articles(query=symbol, article_count=count)

        return news_df

    def analyze_sentiment_textblob(self, text):
        cleaned_text = self.clean_text(text)
        blob = TextBlob(cleaned_text)
        polarity = blob.sentiment.polarity
        if polarity > 0.1: return 'Positive', polarity
        elif polarity < -0.1: return 'Negative', polarity
        else: return 'Neutral', polarity

    def analyze_sentiment_vader(self, text):
        cleaned_text = self.clean_text(text)
        scores = self.vader_analyzer.polarity_scores(cleaned_text)
        compound = scores['compound']
        if compound >= 0.05: return 'Positive', compound
        elif compound <= -0.05: return 'Negative', compound
        else: return 'Neutral', compound

    def analyze_and_get_sentiments(self, news_df):
        vader_results = news_df['text'].apply(lambda text: self.analyze_sentiment_vader(text))
        news_df['sentiment_vader'], news_df['score_vader'] = zip(*vader_results)
        textblob_results = news_df['text'].apply(lambda text: self.analyze_sentiment_textblob(text))
        news_df['sentiment_textblob'], news_df['score_textblob'] = zip(*textblob_results)
        return news_df