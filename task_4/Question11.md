# Question-11 Highest Revenue, Highest Profit?
## Aim
To group the data by subject and compute mean,std,minimum,amximum marks in one aggreagate call and to rank the subjects by mean and standard deviation.

## Code
```python
import numpy as np
import pandas as pd
sales = pd.DataFrame({
    'product': ['Phone Case', 'Phone Case', 'Earbuds', 'Earbuds', 'Smart Watch', 'Smart Watch',
                'Power Bank', 'Power Bank', 'Screen Guard', 'Screen Guard'],
    'month': ['Aug', 'Sep'] * 5,
    'units': [180, 120, 100, 50, 50, 40, 90, 110, 300, 200],
    'price': [299, 299, 1499, 1499, 2999, 2999, 999, 999, 99, 99],
    'cost': [120, 120, 1300, 1300, 2700, 2700, 650, 650, 40, 40]})
sales['revenue']=sales['units']*sales['price']
sales['profit']=sales['revenue']-sales['cost']*sales['units']
grouped_sales=sales.groupby('product')[['revenue','profit']].sum()
grouped_sales['proft margin']=(grouped_sales['profit']/grouped_sales['revenue'])*100
print(grouped_sales.sort_values(by='profit', ascending=False))
```

## Output
```text
              revenue  profit  proft margin
product                                    
Power Bank     199800   69800     34.934935
Phone Case      89700   53700     59.866221
Earbuds        224850   29850     13.275517
Screen Guard    49500   29500     59.595960
Smart Watch    269910   26910      9.969990
```

## Explanation
groupby() function is used to create groups of the data based on the attributes you provide. sort_values() is used to sort the data in ascending or descending order.


## Decision
Promotion Budget: The power bank deserves the promotion budget as it brings the maximum profit while maintaining a good profit
 
Successful only due to  price: The smart watch looks successful only becuase of its high price tag. It brings the highest revenue but it also has high production cost which reduces the profit margin.