import numpy as np
import pandas as pd
orders = pd.DataFrame({
    'order_id': [101, 102, 103, 101, 104, 105, 106, 105],
    'customer': ['Asha', 'ravi', 'Meera', 'Asha', 'Kiran', 'ravi', 'Meera', 'Ravi'],
    'product': ['laptop bag', 'Laptop Bag ', 'desk lamp', 'laptop bag', 'DESK LAMP', 'notebook', 'Notebook', 'Notebook '],
    'amount': [1200, 1200, 900, 1200, 900, 150, 150, 150]})
print(orders)
initial_revenue=orders['amount'].sum()
x=orders.shape
print("rowcount:",x[0])
print("Total revenue before cleaning",initial_revenue)
orders=orders.drop_duplicates()
print(orders)
x=orders.shape
print("rowcount after removing duplicates",x[0])
orders["customer"]=orders["customer"].str.strip().str.capitalize()
orders["product"]=orders["product"].str.strip().str.capitalize()
orders=orders.drop_duplicates()
final_revenue=orders['amount'].sum()
print(orders)
print("Total revenue after cleaning",final_revenue)
inlation_percent=(initial_revenue-final_revenue)/final_revenue*100
print("Inflated revenue figure",inlation_percent)

