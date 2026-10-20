import pandas as pd
import numpy as np
data=pd.DataFrame(pd.read_csv(r"C:\Users\Aradhya Jain\Desktop\Synergy Projects\AradhyaJain_SynergyJTP\task_5\messy_students.csv"))
data=data.drop_duplicates()
data['domain']=data['domain'].str.title().str.strip()
data['name']=data['name'].str.title().str.strip()
data['attendance_percent']=data['attendance_percent'].str.strip("%")
data['height']=data['height'].apply(lambda x: x.replace('m','').strip().int() if not str(x).endswith('cm') else x.replace('cm','').strip())
print(data.to_string())