#THE PURPOSE OF THIS FILE IS TO STORE CONFIGURATIONS OF THE APP
#IT HANDLES THE SECRET AND NON-SECRET SETTINGS OF APP WHERE SECRET SETTING STORES API KEYS.
#THIS PROGRAM SENDS BEARER TOKEN TO SCRAPER WHICH THEN FETCHES TWEETS TO BE ANALYZED.

import os #this import is used to access environment variables.
from dotenv import load_dotenv #this import is used to load environment variables from a .env file.
from dataclasses import dataclass, field #dataclass is used to create classes that are primarily used to store data.
from typing import List #List is used to specify a list type for class attributes.

load_dotenv() # Load environment variables from .env file

@dataclass #dataclass is used to create a class that will hold the configuration for the app.
class AppConfig:
    app_title: str = "Stock Sentiment Analyzer"
    layout: str = "wide"
    default_lang: str = "en"
    default_symbols: List[str] = field(default_factory=lambda: ["TSLA", "AAPL", "MSFT", "GOOGL"])

@dataclass
class NewsApiConfig:
    api_key: str = os.getenv('NEWS_API_KEY') # Fetching News API key from environment variables
    def __post_init__(self): #this method is called after the class is initialized to ensure that the bearer token is set.
        if not self.api_key:
            raise ValueError("News API Bearer Token not found. Please check your .env file.")

class ConfigManager:
    def __init__(self):
        self.app = AppConfig()
        self.news = NewsApiConfig()

config = ConfigManager()