# Question-14 Delhi's Traffic and Air Quality
## Aim
Combine them with concat (reset the index) and add a week column. Compute the correlation between vehicles and PM2.5 and the mean PM2.5 for each week. Interpret: if the city declares an alert when the weekly mean exceeds 70, which week triggers it? Name one other factor besides traffic that could also influence PM2.5.

## Code
```python
import pandas as pd
week1 = pd.DataFrame({'vehicles_k': [30, 35, 40, 45], 'pm25': [52, 55, 60, 63]})
week2 = pd.DataFrame({'vehicles_k': [50, 55, 60, 65], 'pm25': [68, 72, 75, 80]})
combined = pd.concat([week1, week2], ignore_index=True)
print("Shape before adding week column:", combined.shape)
combined['week'] = ['Week 1',] * len(week1) + ['Week 2',] * len(week2)
correlation = combined['vehicles_k'].corr(combined['pm25'])
print("Correlation: {}".format(correlation))
weekly_means = combined.groupby('week')['pm25'].mean()
print("\nWeekly Mean PM2.5:")
print(weekly_means)
```

## Output
```text
Shape before adding week column: (8, 2)
Correlation: 0.9986204405383659

Weekly Mean PM2.5:
week
Week 1    57.50
Week 2    73.75
Name: pm25, dtype: float64s
```

## Explanation
pd.concat() stacks week1 and week2 vertically into a single large DataFrame called combined.
ignore_index=True re-indexes the rows continuously from 0 to 7.
It then prints the shape of the dataset, which output as (8, 2) (8 rows, 2 columns).
.corr() calculates the Pearson correlation coefficient between vehicle counts and PM2.5 levels.
.groupby('week') splits the data back into groups matching 'Week 1' and 'Week 2'.
['pm25'].mean() calculates the average air pollution score for each respective week.

## Interpretation
Alert Trigger: Week 2 triggers the alert because its average PM2.5 value of 73.75 exceeds the city safety threshold of 70.

Other Contributing Factors: Besides vehicular traffic, PM2.5 levels can be influenced by industrial emissions / factory smoke, crop residue burning, construction dust, or weather conditions































