# Question-6 Online Store Catalog Search
## Aim
to count total number of products which contain pro in their names, their price is between 300 and 1500, whose quantity sold is less than 70, which lie in home and stationery categories

## Code
```python
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
```

# Output
```text
              product     category  price  units_sold
0     USB-C Hub Pro  Electronics   1299          85
1       Notebook A5   Stationery    120         400
2      Gel Pen Pack   Stationery     90         520
3  Laptop Stand Pro  Electronics   1599          60
4         Desk Lamp         Home    899         110
5      Mouse Pad XL  Accessories    349         230
6        Webcam Pro  Electronics   2499          25
7      Sticky Notes   Stationery     60         610
Products whose name contains Pro
3
Products in the home or stationary categories
4
products priced between 300 and 1500 inclusive
3
Pro products that sold fewer than 70 units.
2
```

# Explanation
(df['product'].str.contains('Pro')).sum() is used to count the total number of products which contain pro in their names.

# Interpretation
d suggests that products whose price lies in the premium range are sold in less quantity relative to other products.