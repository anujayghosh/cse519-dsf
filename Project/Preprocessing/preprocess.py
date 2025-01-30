import pandas as pd
import numpy as np
import json
import ast

data = pd.read_csv("yelp_businesses.csv")

# Drop all duplicate ids
data = data.drop_duplicates(subset=['id'])

# Makes 2 different columns for latitude and longitudes
def extract_coordinates(coordinates):
    try:
        parsed_dict = ast.literal_eval(coordinates.replace("'", "\""))
        return parsed_dict.get('latitude'), parsed_dict.get('longitude')
    except (SyntaxError, ValueError):
        return None, None

# Converts price strings (eg $$$) to a numerical value (eg 3)
def convert_to_num(price):

    if price == "nan":
        return 0
    return len(price)

def extract_zip_code(location):
    try:
        parsed_dict_loc = ast.literal_eval(location)
        return parsed_dict_loc.get('zip_code'), parsed_dict_loc.get('address1')
    except (SyntaxError, ValueError):
        return None, None

data['latitude'], data['longitude'] = zip(*data['coordinates'].apply(lambda x: extract_coordinates(x)))
data['price'] = data['price'].apply(lambda x: convert_to_num(str(x)))
data['zip_codes'], data['address'] = zip(*data['location'].apply(lambda x: extract_zip_code(x.replace("'", "\""))))

data.to_csv("yelp_preprocessed.csv")