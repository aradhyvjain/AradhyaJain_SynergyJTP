import numpy as np
import pandas as pd
events={"event":["City Sc,ping","Salutes and ladders","Open Mic","Valorant Tournament"]
        ,"registered":[180,95,140,60,120]
        ,"attended":[150,70,135,52,160]
        ,"fee":[200,150,0,50,100]}
data=pd.DataFrame(events)