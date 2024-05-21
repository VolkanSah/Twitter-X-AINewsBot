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
