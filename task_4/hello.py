import numpy as np
import pandas as pd
catalog = {'product': ['USB-C Hub Pro', 'Notebook A5', 'Gel Pen Pack', 'Laptop Stand Pro', 'Desk Lamp', 'Mouse Pad XL', 'Webcam Pro', 'Sticky Notes'], 'category': ['Electronics', 'Stationery', 'Stationery', 'Electronics', 'Home', 'Accessories', 'Electronics', 'Stationery'], 'price': [1299, 120, 90, 1599, 899, 349, 2499, 60], 'units_sold': [85, 400, 520, 60, 110, 230, 25, 610]}
df=pd.DataFrame(catalog)
print(df)
print("Products whose name contains Pro")
print((df['product'].str.contains('Pro')).sum())
print("Products in the home or stationary categories")
print(((df["category"]=='Stationery') | (df['category']=='Home')).sum())
print("products priced between 300 and 1500 inclusive")
print(((df['price']>=300) & (df['price']<=1500)).sum())
print("Pro products that sold fewer than 70 units.")
print((df['units_sold']<70).sum())
