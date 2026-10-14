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