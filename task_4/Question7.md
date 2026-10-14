# Question-7 The faulty Manipal Weather station
## Aim
to count missing values per column and number of rows having atleast one missing value. To delete all the rows where both the columns are nan and to fill the reamain columns nan with their respective column median.

## Code
```python
import numpy as np
import pandas as pd
weather = pd.DataFrame({'day': range(1, 11),
                        'temp_c': [28.1, 29.0, np.nan, 30.2, 29.5, 55.0, np.nan, 27.8, 28.6, 29.3],
                        'humidity': [64, 61, 63, np.nan, 60, 58, np.nan, 66, 65, 62]})
print(weather)
print("Missing values per column")
print(weather.isnull().sum())
print("Rows with atleast one missing value")
print(weather.isnull().any(axis=1).sum())
weather=weather.dropna(subset=['temp_c','humidity'],how='all')
print(weather)
weather['temp_c']=weather['temp_c'].fillna(weather['temp_c'].median())
weather['humidity']=weather['humidity'].fillna(weather['humidity'].median())
print(weather)
```

# Output
```text
   day  temp_c  humidity
0    1    28.1      64.0
1    2    29.0      61.0
2    3     NaN      63.0
3    4    30.2       NaN
4    5    29.5      60.0
5    6    55.0      58.0
6    7     NaN       NaN
7    8    27.8      66.0
8    9    28.6      65.0
9   10    29.3      62.0
Missing values per column
day         0
temp_c      2
humidity    2
dtype: int64
Rows with atleast one missing value
3
   day  temp_c  humidity
0    1    28.1      64.0
1    2    29.0      61.0
2    3     NaN      63.0
3    4    30.2       NaN
4    5    29.5      60.0
5    6    55.0      58.0
7    8    27.8      66.0
8    9    28.6      65.0
9   10    29.3      62.0
   day  temp_c  humidity
0    1   28.10      64.0
1    2   29.00      61.0
2    3   29.15      63.0
3    4   30.20      62.5
4    5   29.50      60.0
5    6   55.00      58.0
7    8   27.80      66.0
8    9   28.60      65.0
9   10   29.30      62.0
```

# Explanation
weather.isnull().sum() is used to count total number of null values every column
weather.isnull().any(axis=1).sum() is used to count the total number of rows having atleast 1 null value. any is used to check atleast 1 null condition and axis=1 is used to horizontally check the dataframe. if you want to count total number of null values per row then you can use weather.isnull().sum(axis=1)
dropna() is used to delete a row having at least one null value
dropna(how='all') is used to delete a row where all values are null
weather=weather.dropna(subset=['temp_c','humidity'],how='all') subset is used when you want to delete a rown with specefic columns having null.
fillna() is used to replace the null values with another value.
fillna(weather['humidity'].median()) - replaces the null values of column humidity with the median of rest of the values of humidity column

# Interpretation
Median is a safer value fill here becuase the sensor fault of 55 degree celsius spikes the mean whereas the median takes the middle value when values are arranged sorted order. Therefore median is safer.
