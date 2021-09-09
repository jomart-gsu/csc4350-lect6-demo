import requests
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
params = {
    "q": "election",
    "api-key": os.getenv("API_KEY"),
}

response = requests.get(
    "https://api.nytimes.com/svc/search/v2/articlesearch.json",
    params=params
)

response_json = response.json()

for i in range(10):
    try:
        print(response_json["response"]["docs"][i]["headline"]["main"])
    except KeyError:
        print("Couldn't fetch headlines")
        break