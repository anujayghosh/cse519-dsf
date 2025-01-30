import pandas as pd

# Load the existing data from the CSV file
existing_csv_file = "yelp_preprocessed.csv"
existing_data = pd.read_csv(existing_csv_file)

# Add new columns for reviews with default values
existing_data['review_texts'] = ""
existing_data['review_ratings'] = ""
existing_data['review_times'] = ""

# Save the updated data to a new CSV file
updated_csv_file = "yelp_reviews.csv"
existing_data.to_csv(updated_csv_file, index=False)

print("Columns for reviews added to CSV.")
