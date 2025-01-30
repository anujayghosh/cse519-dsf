import requests
from bs4 import BeautifulSoup
import pandas as pd
from random import randint
from time import sleep
import re


data = pd.read_csv("../yelp_preprocessed.csv")

unique_zips = data['zip_codes'].unique()
walk_score_df = pd.DataFrame()

walk_score_df['zip_codes'] = unique_zips

walk_scores = []

for zip_code in unique_zips:

    try: 
        r = requests.get(f"https://www.walkscore.com/NY/New_York/{zip_code}")
        soup = BeautifulSoup(r.text, 'html.parser')
        img_tag = soup.find('div', class_='score-info-link').find('img')

        score = img_tag['alt'].split(' ')[0]
        print(f"zipcode: {zip_code} score: {score}")

        walk_scores.append(score)

    except Exception as e:
        print(f"Couldn't get the walk score for zipcode {zip_code} because of error {e}")

    print(f"sleeping for some time...\n")
    sleep(randint(5,20))


walk_score_df['walk_scores'] = walk_scores

walk_score_df.to_csv("zipcode_walkscore.csv")


