import os
import requests
from pymongo import MongoClient
from urllib.parse import quote_plus
import matplotlib.pyplot as plt
import numpy as np
import logging

# Main Function
def main() -> None:
    collection = connect_to_mongodb()
    fetch_data(collection)
    anime_titles, anime_scores, _ = get_data_from_db(collection)
    plot_anime_scores(anime_titles, anime_scores)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# MongoDB Connection
def connect_to_mongodb() -> MongoClient:
    try:
        username = quote_plus(os.getenv("MONGO_USER", "test-user"))
        password = quote_plus(os.getenv("MONGO_PASS", "test-user"))
        uri = f"mongodb+srv://{username}:{password}@testCluster.h7h9r.mongodb.net/?retryWrites=true&w=majority&appName=testCluster&tlsAllowInvalidCertificates=true"
        client = MongoClient(uri)
        logging.info("Connected to MongoDB successfully")
        return client["anime_db"]["top_anime"]
    except Exception as e:
        logging.error(f"Failed to connect to MongoDB: {e}")
        exit(1)

# Fetch data from API
def fetch_data(collection: MongoClient) -> None:
    url = "https://api.jikan.moe/v4/top/anime"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        anime_data = response.json()["data"]
        logging.info("Successful connection to API")

        for anime in anime_data:
            anime_doc = {
                "titulo": anime["title"],
                "puntuacion": anime.get("score", 0),
                "episodios": anime.get("episodes", 0),
            }
            collection.update_one(
                {"titulo": anime_doc["titulo"]},
                {"$setOnInsert": anime_doc},
                upsert=True
            )
    except requests.RequestException as e:
        logging.error(f"API request failed: {e}")
        exit(1)

# Retrieve data from MongoDB
def get_data_from_db(collection: MongoClient) -> tuple[list[str], list[float], list[int]]:
    anime_titles = [anime["titulo"] for anime in collection.find()]
    anime_scores = [anime["puntuacion"] for anime in collection.find()]
    anime_episodes = [anime["episodios"] for anime in collection.find()]
    return anime_titles, anime_scores, anime_episodes

# Plot anime scores
def plot_anime_scores(anime_titles: list[str], anime_scores: list[float]) -> None:
    x = np.arange(len(anime_scores))
    width = 0.35

    fig, ax = plt.subplots(figsize=(14, 8))
    rects1 = ax.bar(x - width / 2, anime_scores, width, label='Anime')

    ax.set_ylabel('Scores')
    ax.set_title('Anime Score')
    ax.set_xticks(x)
    ax.set_xticklabels(anime_titles, rotation=45, ha='right', fontsize=10)

    ax.legend()

    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate(f'{height:.2f}',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects1)
    fig.tight_layout()
    fig.subplots_adjust(top=0.85, bottom=0.3)
    plt.show()


if __name__ == "__main__":
    main()
