# news_scraper.py

import pandas as pd
from newsapi import NewsApiClient
from config import config # Import our configuration manager
import logging

class NewsDataScraper:
    def __init__(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)
        
        try:
            self.client = NewsApiClient(api_key=config.news.api_key)
            if not self.client:
                raise Exception("NewsAPI authentication failed. Check your API Key.")
            self.logger.info("NewsAPI client authenticated successfully.")
        except Exception as e:
            self.logger.error(f"Error during NewsAPI client initialization: {e}")
            raise

    def fetch_articles(self, query, article_count=100):
        try:
            self.logger.info(f"Fetching up to {article_count} articles for query: '{query}'")
            response = self.client.get_everything(
                q=query,
                language='en',
                sort_by='relevancy',
                page_size=100 
            )
            articles_data = []
            if response['status'] == 'ok':
                for article in response['articles']:
                    articles_data.append({
                        'text': f"{article['title']}. {article['description']}", # Combine title and description for more text to analyze
                        'created_at': article['publishedAt']
                    })
            
            df = pd.DataFrame(articles_data).head(article_count)
            self.logger.info(f"Successfully fetched {len(df)} articles.")
            return df

        except Exception as e:
            self.logger.error(f"Error fetching articles from NewsAPI: {e}")
            return pd.DataFrame() # Return an empty DataFrame on error