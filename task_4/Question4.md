# Question-4 Mess Rush Hour
## Aim
To create a dataframe and set hours as index. to access rows with 11 to 13 hours using loc and to select rows at position 3 and 4 using i loc. To find the busy hours using boolean mask

## Code
```python
import numpy as np
import pandas as pd
canteen = {'hour': [8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 'sold': [40, 55, 35, 90, 210, 180, 60, 30, 70, 95], 'prepared': [50, 60, 50, 100, 220, 230, 80, 60, 90, 110]}
df=pd.DataFrame(canteen)
df=df.set_index('hour')
print(df)
# using loc to sold from hours 11 to 13
print(df.loc[11:13,'sold'])
#using iloc to select rows at position 3 and 4
print(df.iloc[2:4])
# using boolean mask to find the busy hours at least 90 items sold
print(df['sold']>90)
```

# Output
```text
    sold  prepared
hour                
8       40        50
9       55        60
10      35        50
11      90       100
12     210       220
13     180       230
14      60        80
15      30        60
16      70        90
17      95       110
hour
11     90
12    210
13    180
Name: sold, dtype: int64
      sold  prepared
hour                
10      35        50
11      90       100
hour
8     False
9     False
10    False
11    False
12     True
13     True
14    False
15    False
16    False
17     True
Name: sold, dtype: bool
```

# Explanation
df=df.set_index('hour') is used to set index as hour
(df.loc[11:13,'sold']) is used to display rows with hours from 11 to 13 both inclusive and sold column
(df.iloc[2:4]) is used to display rows from index 2 to 3


# Interpretation
Both of them look like slicing but only iloc uses slicing. iloc is used for index based slicing, therefore 5 is exclusive but loc is basedon labels therefore 11:13 is used to display rows from 11 to 13