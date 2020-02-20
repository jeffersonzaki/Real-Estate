import pandas as pd
import numpy as np

# Choosing certain columns that will be used
house_df = pd.read_csv("Data/kc_house_data.csv")[["price", "bathrooms", "floors", "waterfront"]]

house_df.dropna(inplace=True)  # Dropping missing values

# Creating separate dataframes with houses with or without waterfronts
waterfront1 = house_df.loc[house_df.waterfront == 1.0]
waterfront0 = house_df.loc[house_df.waterfront == 0.0]

# Creating a separate dataframe that shows floors of the properties
floor1 = house_df.loc[house_df.floors == 1]
floor2 = house_df.loc[house_df.floors == 2]

# Creating a dataframe that shows rows that shows the number of desired bathrooms
bathrooms_more_than_2 = house_df.loc[house_df.bathrooms > 2]
bathrooms_less_and_2 = house_df.loc[house_df.bathrooms <= 2]

# Standard deviation of price of houses with waterfronts
waterfront1_std = waterfront1.price.std()
# Standard deviation of price of houses without waterfronts
waterfront0_std = waterfront0.price.std()

# Standard deviation of price of houses with 1 floor
floor1_std = floor1.price.std()
# Standard deviation of price of houses with 2 floors
floor2_std = floor2.price.std()

# Standard deviation of price of houses that are less than or equal to 2 bathrooms
bathrooms_more_than_2_std = bathrooms_more_than_2.price.std()
# Standard deviation of price of houses that are less than or equal to 2 bathrooms
bathrooms_less_and_2_std = bathrooms_less_and_2.price.std()

def Cohen_d(group1, group2):

    # Compute Cohen's d.

    # group1: Series or NumPy array
    # group2: Series or NumPy array

    # returns a floating point number 

    diff = group1.mean() - group2.mean()

    n1, n2 = len(group1), len(group2)
    var1 = group1.var()
    var2 = group2.var()

    # Calculate the pooled threshold as shown earlier
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    
    # Calculate Cohen's d statistic
    d = diff / np.sqrt(pooled_var)
    
    return d
