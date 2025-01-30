import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz, process

df = pd.read_csv(r"Colab Notebooks/yelp_chainness.csv")

freq_stores = pd.DataFrame(df['name'].value_counts())
freq_stores = freq_stores.reset_index().rename(columns={'index': 'businesses'})

freq_stores = freq_stores.rename(columns = {'name': 'f(n)'})

THRESHOLD = 3
def get_threshold_flag(f):

    if f > THRESHOLD:
        return 1
    return 0

freq_stores['g(n)'] = freq_stores['f(n)'].apply(lambda x: get_threshold_flag(x))

list_of_businesses = list(freq_stores['businesses'])

print(freq_stores)

# 18968(independent) + 815(chain)