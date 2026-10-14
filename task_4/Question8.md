# Question-8 Om Xerox Duplicate orders and messy product names
## Aim
to delete the duplicate data and to find the revenue inflation cause by the duplicate data

## Code
```python
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
```

# Output
```text
   order_id customer      product  amount
0       101     Asha   laptop bag    1200
1       102     ravi  Laptop Bag     1200
2       103    Meera    desk lamp     900
3       101     Asha   laptop bag    1200
4       104    Kiran    DESK LAMP     900
5       105     ravi     notebook     150
6       106    Meera     Notebook     150
7       105     Ravi    Notebook      150
rowcount: 8
Total revenue before cleaning 5850
   order_id customer      product  amount
0       101     Asha   laptop bag    1200
1       102     ravi  Laptop Bag     1200
2       103    Meera    desk lamp     900
4       104    Kiran    DESK LAMP     900
5       105     ravi     notebook     150
6       106    Meera     Notebook     150
7       105     Ravi    Notebook      150
rowcount after removing duplicates 7
   order_id customer     product  amount
0       101     Asha  Laptop bag    1200
1       102     Ravi  Laptop bag    1200
2       103    Meera   Desk lamp     900
4       104    Kiran   Desk lamp     900
5       105     Ravi    Notebook     150
6       106    Meera    Notebook     150
Total revenue after cleaning 4500
Inflated revenue figure 30.0
```

# Explanation
drop_duplicates() is used to delete the rows which have exactly same values for every same column. strip() and .capitalize() are used to remove speaces and convert first letter of every string into capital.
In orders["product"].str.strip().str.capitalize() it is necessary to write .str as python will throw and attribute error orders["product"] accesses series from dataframe and you cannot perform strip on series so .str is used to access the string in the series.


# Interpretation
First attempt missed a duplicate as 'laptop bag' and 'Laptop Bag ' are two different things. They are not same.