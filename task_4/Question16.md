# Question-16 Manipal Weather Swings
## Aim
To know when temperatures swung the most and to plot a line char graph with different markers, linestyles, a legend, a grid and labelled axes and to use numpy to find the day with largest daily range.

## Code
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
days = np.arange(1, 11)
high = np.array([31, 32, 30, 29, 33, 35, 34, 28, 27, 30])
low = np.array([24, 25, 23, 24, 25, 26, 24, 22, 22, 23])
#use of numpy
range=high-low
print("Max range day", days[np.argmax(range)])
print("Day with highest temperature", days[np.argmax(high)])
plt.plot(days,high, marker='.', markersize=10, linewidth=2, linestyle='-', label='High Temperature')
plt.plot(days,low, marker='+', markersize=10, linewidth=2, linestyle='dashed', label='Low Temperature')
plt.xticks(days)
plt.xlabel("Number of Days")
plt.ylabel("Temperature in (degree celsius)", font="arial")
plt.title("Weather of Manipal'\n", fontweight='bold')
plt.grid()
plt.legend(loc='best')
plt.show()
```

## Output
```text
(image in figures section)
Max range day 7
Day with highest temperature 6
```

## Explanation
np.arange(1, 11) automatically sets up a sequence of numbers from 1 to 10 to represent our days.
high and low store the matching temperature readings for each day.
Finding the Daily Ranges: By typing high - low, NumPy automatically subtracts each day's low from its high, giving us a brand new array filled with the 10 separate daily temperature swings.
Finding the Maximums: We use np.max() to extract the largest value out of an array (like finding the biggest swing or the hottest temperature).
Locating the Specific Days: We use np.argmax(). This function scans the array and returns the position index of the highest number. Because Python indexes start counting at 0, we use that position to look up the actual day number inside our days array.

To build the line chart, we use Matplotlib and follow the formatting requested in the prompt:
Differentiating the Lines: We use distinct markers (circles 'o' vs. squares 's'), different line patterns (solid '-' vs. dashed '--'), and contrasting colors so you can tell the lines apart instantly.
Polishing the Layout: We label the x-axis (Time (Days)) and y-axis (Temperature (°C)) while ensuring the units are clearly written.
Final Touches: plt.xticks(days) forces the chart to show labels for every single day from 1 to 10. Finally, plt.grid(True) adds a background grid to make reading the data points easier, and plt.legend() automatically draws a key to identify which line is which.

## Interpretation
NO,
the highest temperature of the period is 35 degree C which happens on day6, however largest temperature swing happens on day 7 which is equal to 10 degree C