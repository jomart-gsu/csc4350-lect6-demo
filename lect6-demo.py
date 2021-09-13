import requests
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())





BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
API_KEY = os.getenv("API_KEY")
params = {
    "q": "afghanistan",
    "api-key": API_KEY
}

response = requests.get(
    BASE_URL,
    params=params,
)

response_json = response.json()

try:
    articles = response_json["response"]["docs"]
    for article in articles:
        print(article["headline"]["main"])
except KeyError:
    print("Couldn't fetch articles!")

