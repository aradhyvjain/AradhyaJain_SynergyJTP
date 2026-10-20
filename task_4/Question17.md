# Question-17 Why are Sales Falling?[Pandas+Matplotlib]
## Aim
Values are monthly sales in ₹ lakh. Use Pandas to add a total column, then plot phones, accessories and total as three lines (make the total dashed). Add markers, a legend and a title. 

## Code
```python
import matplotlib.pyplot as plt
import pandas as pd
store = pd.DataFrame({'month': ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'],
                      'phones': [120, 125, 118, 110, 95, 80],
                      'accessories': [60, 62, 65, 66, 70, 75]})
store['Total']=store['phones']+store['accessories']
print(store)
#use of matplotlib
plt.plot(store['month'],store['accessories'], marker='.', ms=10, label='accessories')
plt.plot(store['month'],store['phones'], marker='.', ms=10, label='phones')
plt.plot(store['month'],store['Total'], marker='.', ms=10, linestyle='dashed', label='Total')

plt.title("Sales VS Months\n", fontweight='bold')
plt.xlabel("Months")
plt.legend(loc='best')
plt.ylabel("Monthly sales in lakhs")
plt.grid()
plt.show()
```

## Output
```text
(image in figures section)
  month  phones  accessories  Total
0   Apr     120           60    180
1   May     125           62    187
2   Jun     118           65    183
3   Jul     110           66    176
4   Aug      95           70    165
5   Sep      80           75    155
```

## Explanation
To find the total revenue each month, we create a new column named total. Pandas handles this easily: store['phones'] + store['accessories'] adds the two categories row-by-row for each month instantly.
Building the Line Graph: We use plt.plot() three separate times to layer our lines onto the same chart.
pass marker='o' to each line so that actual data points stand out as dots.
For the total line, add linestyle='--' to turn it from a solid line into a dashed line.
use plt.title(), plt.xlabel(), and plt.ylabel() to label everything clearly. Finally, plt.legend() automatically reads the label strings we assigned in the plotting step and builds a handy color-coded key in the corner

## Interpretation
Is the owner's claim true? No, it is not true that everything is declining.
Which category is growing? The accessories category is growing steadily
Which category drives the fall? The phones category drives the overall decline, dropping significantly by -40 lakh. Because the drop in phone sales is much larger than the growth in accessories, the total sales drop overall by -25 lakh over the period.