Stock Sentiment Analyzer
📌 Overview

The Stock Sentiment Analyzer is a web-based tool that evaluates real-time market sentiment for any publicly traded company based on recent discussions and news. It collects data from social media (Twitter/X) and/or financial news sources, applies sentiment analysis, and produces a simplified Buy / Hold / Sell recommendation with a confidence score.

The project is designed to demonstrate:
1. Data fetching from live APIs.
2. Natural Language Processing (NLP) for sentiment classification
3. Integration of financial context into AI/ML outputs
4. Interactive and user-friendly deployment

Key Features
1. Ticker Validation:
    - User enters a valid stock ticker (e.g., AAPL, TSLA, RELIANCE.NS).
    - System verifies the ticker against official stock listings to ensure accuracy.
2. Live Data Collection:
    - Social Media Sentiment: Fetches recent tweets mentioning the stock to capture retail investor mood.
    - News Sentiment: Retrieves headlines from financial news APIs to understand media coverage tone.
    - Option to toggle between social media, news, or both.
3. Sentiment Analysis:
    - Uses pre-trained NLP models (e.g., VADER, TextBlob, or HuggingFace transformers) to classify each fetched text as Positive, Neutral, or Negative.
    - Calculates overall sentiment score for the stock.
4. Recommendation Engine
    - Converts sentiment score into Buy / Hold / Sell labels.
    - Displays confidence level (percentage) based on aggregated sentiment distribution.
5. Interactive Dashboard
    - Built with Streamlit for an easy-to-use web interface.
    - Displays:
        -- Sentiment distribution chart
        -- Sample tweets/headlines
        -- Historical trend of sentiment (if enabled)
6. Deployment
    - Hosted on Streamlit Cloud or any preferred hosting platform.
    - Accessible via a shareable public URL.

Tech Stack
Backend & Data Processing:
Python 3.x
Pandas & NumPy (data handling)
Requests / HTTPX (API calls)
NLP library: VADER, TextBlob, or HuggingFace Transformers
Data Sources (Example):
Twitter/X – via Tweepy API or unofficial scrapers
News APIs – e.g., Finnhub, NewsAPI, Yahoo Finance RSS feeds
Frontend & Deployment:
Streamlit (UI & deployment)
Matplotlib / Plotly (visualizations)