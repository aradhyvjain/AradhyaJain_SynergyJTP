# Q22. Which Level Is Unfair? [Pandas + Matplotlib]
## Aim
These are completion times in minutes. Draw side-by-side box plots for the three levels. Then use Pandas to compute the median and IQR of each level and apply the 1.5 × IQR rule to list any outliers. Interpret: which level has an unusual completion time, and should the designers worry about the level or about one player?

## Code
```python
import pandas as pd
import matplotlib.pyplot as plt
times = pd.DataFrame({
    'Level 1': [5, 6, 6, 7, 7, 8, 8, 9],
    'Level 2': [10, 11, 12, 12, 13, 14, 15, 40],
    'Level 3': [15, 16, 18, 18, 19, 20, 22, 24]})
plt.figure(figsize=(8, 5))
times.boxplot()
plt.title('Completion Times by Level')
plt.ylabel('Time (minutes)')
plt.show()
for col in times.columns:
    q1 = times[col].quantile(0.25)
    median = times[col].median()
    q3 = times[col].quantile(0.75)
    iqr = q3 - q1
    lower_fence = q1 - 1.5 * iqr
    upper_fence = q3 + 1.5 * iqr
    outliers = times[col][(times[col] < lower_fence) | (times[col] > upper_fence)].tolist()
```

## Output
```text
Level 1
Median: 7.0
IQR: 2.0
Upper Fence: 11.0
Outliers: None

Level 2
Median: 12.5
IQR: 2.5
Upper Fence: 18.0
Outliers: [40]

Level 3
Median: 18.5
IQR: 3.0
Upper Fence: 25.0
Outliers: None
```

## Explanation
times = pd.DataFrame({ ... }): Creates a data table (DataFrame) containing completion times for three different levels.
'Level 1': [5, 6, 6, 7, 7, 8, 8, 9],: Defines the first column named "Level 1" with its list of time values.
'Level 2': [10, 11, 12, 12, 13, 14, 15, 40],: Defines the second column named "Level 2" with its list of time values.
'Level 3': [15, 16, 18, 18, 19, 20, 22, 24]}): Defines the third column named "Level 3" and closes the DataFrame creation.
plt.figure(figsize=(8, 5)): Sets the size of the plot window to 8 inches wide and 5 inches high.
times.boxplot(): Generates a box plot for each level to show the distribution of the data.
plt.title('Completion Times by Level'): Adds a title at the top of the graph.
plt.ylabel('Time (minutes)'): Labels the vertical y-axis as "Time (minutes)".
plt.show(): Displays the generated box plot on your screen.
for col in times.columns:: Starts a loop to look through each column (Level 1, Level 2, Level 3) one by one.
q1 = times[col].quantile(0.25): Calculates the 1st quartile (25th percentile) for the current column.
median = times[col].median(): Calculates the median (50th percentile) for the current column.
q3 = times[col].quantile(0.75): Calculates the 3rd quartile (75th percentile) for the current column.
iqr = q3 - q1: Finds the Interquartile Range (IQR) by subtracting Q1 from Q3.
lower_fence = q1 - 1.5 * iqr: Calculates the lower limit boundary to identify unusually small values.
upper_fence = q3 + 1.5 * iqr: Calculates the upper limit boundary to identify unusually large values.
outliers = times[col][(times[col] < lower_fence) | (times[col] > upper_fence)].tolist(): Filters out data points beyond the fences and saves them as a list of statistical outliers (like the number 40 in Level 2).

## Interpretation
Yes, the user improved significantly during the second week.
Goal Attainment: The user met their daily 8,000-step goal on 5 days in Week 2, compared to only 4 days in Week 1.
Higher Average Volumne: The weekly mean increased from ~8,142.86 steps in Week 1 to ~8,928.57 steps in Week 2.
Higher Floor: The user's lowest-performing day in Week 2 (Saturday: 5,000 steps) was better than their lowest day in Week 1 (Saturday: 3,000 steps).

