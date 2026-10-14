# Question-5 Is the busiest hour the most useful
## Aim
To add waste and waste percentage columns and then find the hours with max items sold , mas absolute waste and max waste percentage

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
df['waste']=df['prepared']-df['sold']
df['waste_pct']=(df['waste']/df['prepared'])*100
print(df)
print("The hour with most items sold")
print(df['sold'].idxmax())
print("The hour with highest absolute waste")
print(df['waste'].idxmax())
print("The hour with highest waste percentage")
print(df['waste_pct'].idxmax())
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
      sold  prepared  waste  waste_pct
hour                                  
8       40        50     10  20.000000
9       55        60      5   8.333333
10      35        50     15  30.000000
11      90       100     10  10.000000
12     210       220     10   4.545455
13     180       230     50  21.739130
14      60        80     20  25.000000
15      30        60     30  50.000000
16      70        90     20  22.222222
17      95       110     15  13.636364
The hour with most items sold
12
The hour with highest absolute waste
13
The hour with highest waste percentage
15
```

# Explanation
idxmax() function has been used to find the respective hours.
df['waste']=df['prepared']-df['sold'] has been used to add waste column
df['waste_pct']=(df['waste']/df['prepared'])*100 has been used to add waste percentage columns


# Decision
it depends if you want to save environment then select hour 13 as it will cut the maximum waste but if you want maximum profit then select hour 15 as the least amount of products were sold in that hour.
