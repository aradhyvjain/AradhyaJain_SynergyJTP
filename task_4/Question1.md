# Question-1 Fest attendance check

## Aim
to understand how Dataframe functions work and to find how many registrations are turned into actual attendance

## Code
```python
import numpy as np
import pandas as pd
events={"event":["City Saping","Salutes and ladders","Open Mic","Valorant Tournament","Gaming Arena"]
        ,"registered":[180,95,140,60,120]
        ,"attended":[150,70,135,52,160]
        ,"fee":[200,150,0,50,100]}
data=pd.DataFrame(events)
print("the shape of the data before the new column is added", data.shape)
print("the data types of the dataframe are", data.dtypes)
data["registered_attendance"]=((data["attended"]/data["registered"])*100).round(1)
print(data)
max_registration=data.iat[data["registered"].idxmax(),0]
print(max_registration, "is the event with highest number of registrations")
max_attendancerate=data.iat[data["registered_attendance"].idxmax(),0]
print(max_attendancerate,"is the event with highest attendance rate")
```

# Output
```text
the shape of the data before the new column is added (5, 4)
The data types of the dataframe are event         object
registered     int64
attended       int64
fee            int64
dtype: object
                 event  registered  attended  fee  registered_attendance
0          City Saping         180       150  200                   83.3
1  Salutes and ladders          95        70  150                   73.7
2             Open Mic         140       135    0                   96.4
3  Valorant Tournament          60        52   50                   86.7
4         Gaming Arena         120       160  100                  133.3
City Saping is the event with highest number of registrations
Gaming Arena is the event with highest attendance rate
```

# Explanation
pd.Dataframe() is a type of constructor which created an object called data. data.shape is used to represent (number of rows,number of columns).
data.dtypes is used to display the information of datatypes usedd in the dataframe
iat() function is used to find a particular value through label. data["registered_attendance"].idxmax() is used to find the index of the maximum value where as max function is used to find the value of maximum quantity.
To add a new column syntax object_name["column name"]=values if only one value is passed then that value is applied to all the rows otherwise values in the form of list or tuple should be passed

# Interpretation
No, the highest attendance event and highest registration event aint same. It means you cannot judge an event on the basis of registrations alone as registrations can be high but theres a chance that actual attendance might be low.
