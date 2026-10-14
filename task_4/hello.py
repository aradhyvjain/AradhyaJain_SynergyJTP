import numpy as np
import pandas as pd
events={"event":["City Saping","Salutes and ladders","Open Mic","Valorant Tournament","Gaming Arena"]
        ,"registered":[180,95,140,60,120]
        ,"attended":[150,70,135,52,160]
        ,"fee":[200,150,0,50,100]}
data=pd.DataFrame(events)
print("the shape of the data before the new column is added", data.shape)
data["registered_attendance"]=((data["attended"]/data["registered"])*100).round(1)
print(data)
max_registration=data.iat[data["registered"].idxmax(),0]
print(max_registration, "is the event with highest number of registrations")
max_attendancerate=data.iat[data["registered_attendance"].idxmax(),0]
print(max_attendancerate,"is the event with highest attendance rate")