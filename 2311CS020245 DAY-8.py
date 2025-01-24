#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

# Example DataFrame
data = {
    'Region': ['East', 'West', 'East', 'South', 'North'],
    'Sales': [1500, 800, 1200, 600, 2000],
    'Profit': [300, 50, 240, 40, 400],
    'Quantity': [10, 5, 15, 4, 20]
}
df = pd.DataFrame(data)

# Data Filtering: Extract rows where Sales > 1000
sales_greater_1000 = df[df['Sales'] > 1000]

# Data Filtering: Find sales records for a specific region (e.g., "East")
east_region_sales = df[df['Region'] == 'East']

# Data Processing: Add a new column, Profit_Per_Unit
df['Profit_Per_Unit'] = df['Profit'] / df['Quantity']

# Data Processing: Create a new column, High_Sales
df['High_Sales'] = df['Sales'].apply(lambda x: 'Yes' if x > 1000 else 'No')

# Results
print("Rows with Sales > 1000:")
print(sales_greater_1000)
print("\nSales records for 'East' region:")
print(east_region_sales)
print("\nUpdated DataFrame:")
print(df)

