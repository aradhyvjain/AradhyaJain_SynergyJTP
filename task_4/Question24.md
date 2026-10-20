# Question-24 Telling the Revenue Story [Pandas + Matplotlib]
## Aim
Revenue is in ₹ lakh. Use pct_change to compute month-over-month growth. Plot revenue as a line with markers, write the value above each point, and use annotations with arrows to mark the month with the highest growth and the month with the biggest drop. Set a suitable figure size, axis labels and a title that states the finding. Interpret: write one sentence the founder could present to investors.

## Code
```python
import pandas as pd
import matplotlib.pyplot as plt
revenue = pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'revenue': [12, 15, 21, 19, 24, 22]
})
revenue['growth'] = revenue['revenue'].pct_change() * 100
plt.figure(figsize=(9, 5.5))
plt.plot(revenue['month'], revenue['revenue'], marker='o', color='#1f77b4', linewidth=2.5, markersize=8)

for i, row in revenue.iterrows():
    plt.text(row['month'], row['revenue'] + 0.6, f"₹{row['revenue']}L", ha='center', va='bottom', fontweight='bold')
plt.annotate('Highest Growth\nMar (+40.0%)', 
             xy=('Mar', 21), xytext=('Jan', 22.5),
             arrowprops=dict(facecolor='green', shrink=0.1, width=1.5, headwidth=7),
             fontweight='bold', color='green', bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="green", lw=1))
plt.annotate('Biggest Drop\nApr (-9.5%)', 
             xy=('Apr', 19), xytext=('Jun', 16),
             arrowprops=dict(facecolor='red', shrink=0.1, width=1.5, headwidth=7),
             fontweight='bold', color='red', bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="red", lw=1))
plt.title('H1 Revenue Trend: Strong Growth Peak in May despite April Correction', fontsize=13, fontweight='bold', pad=15)
plt.xlabel('Month', fontsize=11, fontweight='bold')
plt.ylabel('Revenue (in ₹ Lakh)', fontsize=11, fontweight='bold')
plt.ylim(10, 27)
plt.grid(True, linestyle='--', alpha=0.4)
plt.show()
```

## Output
```text
(image in fig section)
```

## Explanation
Line 13 (revenue['growth'] = ...): Calculates the month-over-month percentage change in revenue and saves it as a new column named 'growth'.
Line 14 (plt.figure(figsize=(9, 5.5))): Sets the physical display size of the graph to 9 inches wide by 5.5 inches high.
Line 15 (plt.plot(...)): Plots a blue line chart of revenue against months using circular markers (o) and custom line thicknesses.
Line 17 (for i, row in revenue.iterrows():): Starts a loop to iterate through every single row of the revenue table.
Line 18 (plt.text(...)): Places a bold numerical value (like "21L") slightly above each data point on the chart.
Lines 19–22 (plt.annotate('Highest Growth...', ...)): Creates a green callout box and arrow pointing to March to highlight it as the peak growth month.
Lines 23–26 (plt.annotate('Biggest Drop...', ...)): Creates a red callout box and arrow pointing to April to highlight it as the sharpest revenue dip.

## Interpretation
Despite a minor 9.5% operational correction in April, our core business remains highly scalable, achieving a stellar 40% MoM revenue surge in March and concluding H1 with an upward trend at ₹22 Lakh."
