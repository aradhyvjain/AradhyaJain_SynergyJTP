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
