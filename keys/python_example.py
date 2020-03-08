# Example python script
# Allison Horst
# ESM 244 (Winter 2020)

# Import packages
import pandas as pd
import matplotlib.pyplot as mp

# Read in some data:
ex_data = pd.read_csv('data/my_data.csv')

# Do some exploring:

list(ex_data) # List the column names
ex_data.describe() # Summarize numeric columns
ex_data.head(2) # Show first 2 rows
ex_data.tail(3) # Show last 3 rows

# Add a new column with height converted to feet: 
add_ft = ex_data.assign(height_ft = ex_data['height_m']*3.28)

# Sort animals by height:
by_height = add_ft.sort_values('height_m')

# Filter to only get animals of species "dog":
dogs = by_height.query('species == "dog"')

# Find the mean of numeric columns:
dogs.mean()

# Find the sd of numeric columns: 
dogs.std()

# Make a scatterplot of animal weight x height_m for the original data (ex_data)
mp.scatter(ex_data.weight_lb, ex_data.height_m, s = 100, c = "purple")
mp.show()
