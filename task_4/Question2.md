# Question-2 Fitness tracker week
## Aim
to understand how to do type conversion, use describe function and use idxmin() and idxmax()

## Code
```python
import numpy as np
import pandas as pd
#creating the dataframe
data = np.array([[8200, 7.5, 40], [10400, 6.5, 55], [6100, 8.0, 20], [12000, 6.0, 70], [9800, 7.0, 50], [3000, 9.0, 10], [7500, 8.5, 35]])
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
df=pd.DataFrame(data, index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], columns=["Steps","Sleep_Hours","Active_minutes"])
print(df)
#changing the data type from float to int
df['Steps'] = df['Steps'].astype(int)
df['Active_minutes']=df['Active_minutes'].astype(int)
print(df.dtypes)
#using discribe function
print("using describe function to print average sleep and average steps")
print(df["Steps"].describe(),df['Sleep_Hours'].describe())
#using idxmax() and idxmin()
print("The day with most steps is",df["Steps"].idxmax())
print("The day with least sleep is",df['Sleep_Hours'].idxmin())
```

# Output
```text
              Steps  Sleep_Hours  Active_minutes
Mon   8200.0          7.5            40.0
Tue  10400.0          6.5            55.0
Wed   6100.0          8.0            20.0
Thu  12000.0          6.0            70.0
Fri   9800.0          7.0            50.0
Sat   3000.0          9.0            10.0
Sun   7500.0          8.5            35.0
Steps               int64
Sleep_Hours       float64
Active_minutes      int64
dtype: object
using describe function to print average sleep and average steps
count        7.000000
mean      8142.857143
std       2993.246366
min       3000.000000
25%       6800.000000
50%       8200.000000
75%      10100.000000
max      12000.000000
Name: Steps, dtype: float64 count    7.000000
mean     7.500000
std      1.080123
min      6.000000
25%      6.750000
50%      7.500000
75%      8.250000
max      9.000000
Name: Sleep_Hours, dtype: float64
The day with most steps is Thu
The day with least sleep is Thu
```

# Explanation
pd.Dataframe() is a type of constructor which created an object called df. index and columns are keyword arguments which are used in pd.Dataframe() constructor astype() is used for type conversion. it can convert the data from int to float. describe() is used to show mean std min 25% 50% 75% and max. idxmax() is used to return the label of the maximum value.

# Interpretation
to determin whether busy days actually cause shorter sleep, we need more data from different people in different seasons, from people in different occupations. We can also gather data based on caffeine intake, stress levels and screen time.