import requests
import pandas as pd
import os

# Define your Yelp API key and the base URL
api_key = "jScKMgtYi9e4gxCmuI5gy2GWAfp1EN7Tz-AQRh0aRXkVE9LT50hK5am82-bKiv7N6xV0V7JiWk0LJb-iHRDxiEXf0zCXiN0wy8_nr1ak2CCt-QMPEA7iD657aI1AZXYx"
base_url = "https://api.yelp.com/v3/businesses/search"

# Initialize an empty DataFrame to store the results
results_df = pd.DataFrame()
existing_csv_file = "yelp_businesses.csv"

# Check if the CSV file already exists
if os.path.exists(existing_csv_file):
    # Load the existing data from the CSV
    existing_data = pd.read_csv(existing_csv_file)
    results_df = pd.concat([results_df, existing_data], ignore_index=True)

# Set the maximum number of results you want
max_results = 1000  # You can change this as needed

# Set the step size for the offset parameter
step = 50  # You can change this as needed

for offset in range(0, max_results, step):
    # Define the parameters for the API call
    params = {
        "location": "manhattan",
        "term": "parks",
        "sort_by": "best_match",
        "limit": step,
        "offset": offset,
    }

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    response = requests.get(base_url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        businesses = data.get("businesses", [])
        if not businesses:
            break  # No more results, exit the loop

        # Convert the business data to a DataFrame
        business_df = pd.DataFrame(businesses)

        # Append this DataFrame to the results DataFrame
        results_df = pd.concat([results_df, business_df], ignore_index=True)

    else:
        print(f"Error in API request. Status code: {response.status_code}")
        break

# Save the results to a CSV file
results_df.to_csv(existing_csv_file, index=False)
print("Data saved to CSV.")

# DONE CATEGORIES: restaurants, bars, cafes, convenience, candy, coffee, desserts, diners, pizza, bagel, deli, halal, farmersmarket, foodtrucks, food_court, gaybars, gourmet, pubs, food, nightlife, clubs, pets, zoos, aquariums, farms, wineries, breweries, bakeries
# DONE CATEGORIES: libraries, bookstores, arts, museums, antiques, artsandcrafts, shopping, active, beautysvc, fitness, musicvenues, church, buddhist_temples, hindu_temples, mosques, shrines, sikhtemples, spiritism, synagogues, taoisttemples, health, education, parks