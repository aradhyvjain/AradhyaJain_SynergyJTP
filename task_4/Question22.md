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
    
    print(f"--- {col} ---")
    print(f"Median: {median}")
    print(f"IQR: {iqr:.1f}")
    print(f"Upper Fence: {upper_fence:.1f}")
    print(f"Outliers: {outliers if outliers else 'None'}\n")
