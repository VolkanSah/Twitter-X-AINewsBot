# News Scraper and Twitter Bot (Fuck Elon Musk! X-Bot)

The free world is more at risk than ever. Elon Musk, a villain as foretold in James Bond films, is a threat that must not be underestimated. With his own satellites, his own internet, his own aviation, and his own cars, he has taken control of many aspects of our daily lives. He can control everything. Use this tool to spread the truth. One small click and masses of real news instead of all this fake news and hate on X (formerly Twitter).

## Features

- **Web Scraping**: Extracts news articles from a specified website.
- **AI Text Generation**: Uses OpenAI's GPT-3.5-turbo model to generate short descriptions and tweets for each article.
- **Twitter Automation**: Posts the generated tweets to a Twitter account using the Twitter API.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `openai` library
- `tweepy` library

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/news-scraper-twitter-bot.git
    cd news-scraper-twitter-bot
    ```

2. **Install the required Python packages**:
    ```sh
    pip install requests beautifulsoup4 openai tweepy
    ```

3. **Set up OpenAI and Twitter API keys**:
    - Sign up for an API key at [OpenAI](https://beta.openai.com/signup/).
    - Create a Twitter Developer account and generate API keys at the [Twitter Developer Portal](https://developer.twitter.com/).

## Usage

1. **Edit the script** to include your API keys and the news URL:
    ```python
    ...

    # OpenAI API key
    openai.api_key = 'YOUR_OPENAI_API_KEY'
    ...
    # Twitter API keys
    api_key = "YOUR_API_KEY"
    api_secret_key = "YOUR_API_SECRET_KEY"
    access_token = "YOUR_ACCESS_TOKEN"
    access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

    .... 

    # Main script
    if __name__ == "__main__":
        news_url = 'https://example-news-website.com'  # Replace with a real news website
        news = get_news(news_url)
        for item in news:
            description = generate_description(item['summary'])
            tweet = generate_tweet(item['title'], item['link'])
            post_tweet(tweet)
            print(f"Title: {item['title']}")
            print(f"Link: {item['link']}")
            print(f"Description: {description}")
            print(f"Tweet: {tweet}\n")
    ```

2. **Run the script**:
    ```sh
    python news_scraper_twitter_bot.py
    ```

3. **Example Output**:
    ```sh
    Title: Example News Title
    Link: https://example-news-website.com/article
    Description: This is a short description of the article generated by OpenAI.
    Tweet: Check out this article: Example News Title https://example-news-website.com/article
    ```

## Code Explanation

### Web Scraping

The function `get_news` uses `requests` to fetch the HTML content of the specified news website and `BeautifulSoup` to parse the HTML and extract article titles, links, and summaries.

### AI Text Generation

The functions `generate_description` and `generate_tweet` use OpenAI's GPT-3.5-turbo model to generate a short description and a tweet for each article, respectively.

### Twitter Automation

The function `post_tweet` uses `tweepy` to authenticate with the Twitter API and post the generated tweet to your Twitter account.

## Full Script

```python
import requests
from bs4 import BeautifulSoup
import openai
import tweepy

# OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Twitter API keys
api_key = "YOUR_API_KEY"
api_secret_key = "YOUR_API_SECRET_KEY"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_news(url):
    """
    Scrapes news articles from the specified URL.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article')
    
    news_list = []
    for article in articles:
        title = article.find('h2').text
        link = article.find('a')['href']
        summary = article.find('p').text
        news_list.append({'title': title, 'link': link, 'summary': summary})
    
    return news_list

def generate_description(summary):
    """
    Generates a short description using OpenAI API.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Create a short description for this article: {summary}"}
        ]
    )
    description = response.choices[0].message['content'].strip()
    return description

def generate_tweet(title, link):
    """
    Generates a tweet using OpenAI API.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Create a short tweet about this article: {title}. Include this link: {link}"}
        ]
    )
    tweet = response.choices[0].message['content'].strip()
    return tweet

def post_tweet(tweet):
    """
    Posts a tweet using Tweepy.
    """
    api.update_status(status=tweet)

# Main script
if __name__ == "__main__":
    news_url = 'https://example-news-website.com'  # Replace with a real news website
    news = get_news(news_url)
    for item in news:
        description = generate_description(item['summary'])
        tweet = generate_tweet(item['title'], item['link'])
        post_tweet(tweet)
        print(f"Title: {item['title']}")
        print(f"Link: {item['link']}")
        print(f"Description: {description}")
        print(f"Tweet: {tweet}\n")
```

## Contributing

Feel free to submit pull requests or open issues if you find any bugs or have suggestions for improvements.

## License
This project is licensed under the Fuck Elon Musk License - In your Face , Bro, In your Face!

### Acknowledgements

- OpenAI for providing the AI models.
- Twitter for the API access.
- BeautifulSoup for web scraping.
