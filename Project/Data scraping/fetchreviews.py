import requests
import pandas as pd
import json
import time

api_key = ""
base_url = "https://api.yelp.com/v3/businesses/"

existing_csv_file = "yelp_reviews.csv"
existing_data = pd.read_csv(existing_csv_file)

def fetch_reviews(business_id):
    url = f"{base_url}{business_id}/reviews?limit=3&sort_by=yelp_sort"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        reviews = data.get("reviews", [])
        if reviews:
            # Extract review data
            review_texts = [review['text'] for review in reviews]
            review_ratings = [review['rating'] for review in reviews]
            review_times = [review['time_created'] for review in reviews]

            return {
                'review_texts': json.dumps(review_texts),
                'review_ratings': json.dumps(review_ratings),
                'review_times': json.dumps(review_times)
            }
    return {}

start = 0
batch_size = 500
batch = existing_data.iloc[start:start + batch_size]
for idx, row in batch.iterrows():
    reviews_data = fetch_reviews(row['id'])
    print(idx," reviews length: ", len(reviews_data))
    for col, value in reviews_data.items():
        existing_data.at[idx, col] = value
    time.sleep(0.1) 

existing_data.to_csv(existing_csv_file, index=False)

print("Reviews added to the existing CSV.")
#Done id: 0-19989