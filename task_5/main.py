import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import csv

#reading the data
messy_data=pd.read_csv("messy_students.csv")

#writing the json summary
messy_data_summary={"rows":len(messy_data),"columns":len(messy_data.columns),"missing values":messy_data.isnull().sum().to_dict(),"duplicates": int(messy_data.duplicated().sum()),
    "data_types": messy_data.dtypes.astype(str).to_dict()}
#writing the messy data summary in json file
with open("summary_before.json","w") as f:
    json.dump(messy_data_summary,f)

#dropping duplicate data
messy_data=messy_data.drop_duplicates()

#data validation for submitted column
corrected_submission={"yes":"YES","no":"NO","Y":"YES","N":"NO","Yes":"YES"}
messy_data["submitted"]=messy_data["submitted"].map(corrected_submission)

#data validation for weight column
messy_data["weight"]=messy_data["weight"].str.replace("kg","").str.strip()
messy_data["weight"]=pd.to_numeric(messy_data["weight"],errors="coerce")
messy_data["weight"]=messy_data["weight"].fillna(messy_data["weight"].median())

#data validation for study hours
messy_data["study_hours"]=messy_data["study_hours"].replace("two","2")
messy_data["study_hours"]=pd.to_numeric(messy_data["study_hours"],errors="coerce")

#data validation for score
messy_data["score"]=messy_data["score"].replace("nine","9")
messy_data["score"]=pd.to_numeric(messy_data["score"],errors="coerce")
messy_data["score"]=messy_data["score"].fillna(messy_data["score"].mean())

#data validation for attendance percent
messy_data["attendance_percent"]=messy_data["attendance_percent"].str.replace("%","").str.strip()
messy_data["attendance_percent"]=pd.to_numeric(messy_data["attendance_percent"],errors="coerce")
messy_data.loc[(messy_data["attendance_percent"] < 0) | (messy_data["attendance_percent"] > 100),"attendance_percent"]=np.nan
attendance_median=messy_data["attendance_percent"].median()
messy_data["attendance_percent"]=messy_data["attendance_percent"].fillna(attendance_median)

#domain data validation
domain_mapping = {"ml": "Machine Learning","machine learning": "Machine Learning","web": "Web Development", "web dev": "Web Development","web development": "Web Development","electronics": "Electronics","mechanical": "Mechanical"}
messy_data["domain"] = messy_data["domain"].astype(str).str.lower().str.strip().map(domain_mapping)

#data validation for attendance
def convert_height_to_cm(height):
    height = str(height).lower().strip()
    if "cm" in height:
        return float(height.replace("cm", "").strip())
    if "m" in height:
        return float(height.replace("m", "").strip()) * 100
    return np.nan
messy_data["height"] = messy_data["height"].apply(convert_height_to_cm)

#converting messy data to clean data
clean_data=messy_data

#validation check
validation = {
    "unique_student_ids":clean_data["student_id"].is_unique,
    "attendance_within_range":clean_data["attendance_percent"].between(0, 100).all(),
    "missing_values_remaining":clean_data.isnull().sum().sum()
}
print("Validation Results:")
print(validation,"\n\n")
print(messy_data.to_string())

#writing the json summary for the cleaned data
cleaned_data_summary={"rows":len(clean_data),"columns":len(clean_data.columns),"missing values":clean_data.isnull().sum().to_dict(),"duplicates": int(clean_data.duplicated().sum()),
    "data_types": clean_data.dtypes.astype(str).to_dict()}

#writing the cleaned data summary in json file
with open("summary_after.json","w") as f:
    json.dump(messy_data_summary,f)

#exporting the clean data as csv
with open('clean_data.csv', mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(clean_data)
    print("data has been successfully expoted in the form of csv")

#visualisation part
#domain average score
avg_scores = clean_data.groupby("domain")["score"].mean()
avg_scores.plot(kind="bar")
plt.title("Average Score by Domain")
plt.ylabel("Average Score")
plt.tight_layout()
plt.show()

#Attendance vs score
plt.scatter(clean_data["attendance_percent"],clean_data["score"])
plt.xlabel("Attendance (%)")
plt.ylabel("Score")
plt.title("Attendance vs Score")
plt.tight_layout()
plt.show()

#group wise submission
submission_wise_group=clean_data.groupby("submitted").count()
submission_wise_group["domain"].plot(kind="bar")
plt.title("Submission Status")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

report = """
DATA CLEANING REPORT
Original Records : {}
Final Records    : {}
Duplicates Removed : {}
Validation Results:{}
""".format(messy_data_summary["rows"],cleaned_data_summary['rows'],messy_data_summary['duplicates'],validation)

with open("cleaning_report.md", "w") as file3:
    file3.write(report)
print("Task completed.")



