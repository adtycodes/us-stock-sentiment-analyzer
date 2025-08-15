# US Stock Sentiment Analyzer

A web application that fetches real-time news articles related to a stock symbol, performs sentiment analysis using advanced NLP models, and visualizes the correlation between public sentiment and market performance.

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/adtycodes/us-stock-sentiment-analyzer)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---
## Table of Contents

- [About The Project](#about-the-project)
- [Built With](#built-with)
- [Key Features](#key-features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)
- [Contact](#contact)

---

## About The Project

This project was built to explore the relationship between public sentiment, as reflected in news media, and the financial performance of publicly traded stocks. In today's information-driven market, understanding the narrative around a company is crucial for making informed investment decisions. This tool automates the process of gathering and analyzing this sentiment data.

The application allows a user to enter any valid US stock ticker symbol. It then fetches a multitude of recent news articles from around the web, processes the text of these articles to determine the overall sentiment, and presents the findings in a comprehensive, interactive dashboard. The final goal is to visually correlate the calculated sentiment trends with the stock's historical price and volume data to uncover potential patterns.

<br>

<img width="1919" height="869" alt="image" src="https://github.com/user-attachments/assets/90a0cf37-d00d-4f25-9bf7-738c71e6d3dd" />


<br>

---
## Built With

This project leverages a modern stack of data science and web development tools to deliver a seamless and powerful user experience.

* **Frontend:**
    * [Streamlit](https://streamlit.io/)
* **Backend & Data Analysis:**
    * [Python 3](https://www.python.org/)
    * [Pandas](https://pandas.pydata.org/)
    * [NumPy](https://numpy.org/)
* **Data Sources:**
    * [NewsAPI.org](https://newsapi.org/) for real-time news articles.
    * [yfinance](https://pypi.org/project/yfinance/) for historical stock market data.
* **Natural Language Processing (NLP):**
    * [VADER](https://pypi.org/project/vaderSentiment/) for sentiment analysis tuned for social media and news headlines.
    * [TextBlob](https://textblob.readthedocs.io/en/dev/) for general-purpose sentiment analysis.
* **Data Visualization:**
    * [Plotly](https://plotly.com/python/)
* **Deployment:**
    * [Streamlit Community Cloud](https://streamlit.io/cloud)

---
## Key Features

- **Dynamic Stock Analysis:** Enter any valid stock ticker to fetch relevant data on the fly.
- **Customizable Time Period:** Analyze data over various timeframes, from one month to two years.
- **Real-Time News Aggregation:** Fetches up to 100 of the latest news articles from NewsAPI.org for the selected company.
- **Dual-Model Sentiment Analysis:** Employs both VADER and TextBlob models to provide a robust sentiment score.
- **Comprehensive Overview Dashboard:**
    - At-a-glance metrics including an overall sentiment score (0-10), percentage of positive vs. negative articles, and the stock's price change over the period.
- **In-Depth Trend Analysis:**
    - An interactive line chart to visualize the daily sentiment trend, allowing users to spot shifts in public opinion.
- **Professional Financial Charting:**
    - A detailed candlestick chart displaying the stock's Open, High, Low, and Close prices.
    - An integrated bar chart showing daily trading volume.
- **Core Correlation Analysis:**
    - A powerful dual-axis chart that plots the daily sentiment score directly against the stock's closing price, making it easy to visually inspect for correlations.

---
## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Make sure you have Python 3.8+ and pip installed on your system.

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/adtycodes/us-stock-sentiment-analyzer.git](https://github.com/adtycodes/us-stock-sentiment-analyzer.git)
    cd us-stock-sentiment-analyzer
    ```
2.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```
3.  **Set up your environment variables:**
    - Create a file named `.env` in the root of your project folder.
    - You will need to get a free API key from [NewsAPI.org](https://newsapi.org/).
    - Add your key to the `.env` file like this:
      ```
      NEWS_API_KEY="YOUR_API_KEY_HERE"
      ```
4.  **Run the application:**
    ```sh
    streamlit run main.py
    ```
    A new tab should open in your browser with the application running.

---
## Usage

The application is designed to be simple and intuitive.

1.  Use the sidebar on the left to configure your analysis.
2.  Enter a valid stock ticker (e.g., `GOOGL` for Google).
3.  Select the time period you wish to analyze.
4.  Choose the number of news articles to fetch.
5.  Click the "Analyze" button.

The application will then fetch and process the data, displaying the full dashboard with its four interactive tabs.

<img width="254" height="412" alt="image" src="https://github.com/user-attachments/assets/3ecf65c7-04a1-4e7a-965b-e92f0be9e87a" />


---
## Project Structure

The project is organized into a modular structure to ensure clean code and separation of concerns.
.
  ├── 📂 .github/            # GitHub Actions and workflows
  ├── 📄 .gitignore           # Specifies files for Git to ignore
  ├── 📜 analyzer.py         # The core logic engine for sentiment analysis and data processing
  ├── 📜 config.py           # Manages configuration and securely loads API keys
  ├── 📜 main.py             # The main Streamlit application file for the UI
  ├── 📜 news_scraper.py      # Module responsible for fetching data from NewsAPI.org
  ├── 📜 requirements.txt     # A list of all necessary Python packages for the project
  └── 📜 README.md            # This file

---
## License

This project is distributed under the MIT License. See `LICENSE` for more information.

---
## Contact

Aditya - adityaksin.9451@gmail.com

Project Link: [https://github.com/adtycodes/us-stock-sentiment-analyzer](https://github.com/adtycodes/us-stock-sentiment-analyzer)
