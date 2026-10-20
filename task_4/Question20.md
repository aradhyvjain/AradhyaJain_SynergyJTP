## 20. Traffic Is Not the Whole Story [Pandas + Matplotlib]
## Aim
Plot vehicles (x-axis) against PM2.5 (y-axis). Use a dictionary and map to color points by zone, scale marker size by population, and add a legend that names the zones. Interpret: which stations break the “more traffic means more pollution” pattern, and what variable explains them?

## Code
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
stations = pd.DataFrame({
    'station': ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8'],
    'vehicles_k': [35, 40, 65, 60, 45, 50, 70, 30],
    'pm25': [58, 60, 80, 77, 110, 115, 83, 52],
    'zone': ['Residential', 'Residential', 'Commercial', 'Commercial',
             'Industrial', 'Industrial', 'Commercial', 'Residential'],
    'population_k': [40, 45, 30, 25, 15, 10, 35, 50]})
colors_stations={'Residential':'blue','Commercial':'Red','Industrial':'black'}
stations['color']=stations['zone'].map(colors_stations)
print(stations)
for zone,color in colors_stations.items():
    sub_station=stations[stations['zone']==zone]
    plt.scatter(sub_station['vehicles_k'],sub_station['pm25'], s=60, color=color, label=zone)

plt.xlabel('Vehicles (thousands)')
plt.ylabel('PM2.5')
plt.title('Traffic Volume vs PM2.5 Levels')
plt.legend(title='Zones', loc='best')
plt.grid()
plt.show()
```

## Output
```text
  station  vehicles_k  pm25         zone  population_k  color
0      S1          35    58  Residential            40   blue
1      S2          40    60  Residential            45   blue
2      S3          65    80   Commercial            30    Red
3      S4          60    77   Commercial            25    Red
4      S5          45   110   Industrial            15  black
5      S6          50   115   Industrial            10  black
6      S7          70    83   Commercial            35    Red
7      S8          30    52  Residential            50   blue
```

## Explanation
pd.DataFrame(): Creates the structured data table.
.map(): Converts zone names into colors using a dictionary.
print(): Displays the final data table in the console.
matplotlib Functions
plt.scatter(): Plots the individual data points on the graph.
plt.xlabel() & plt.ylabel(): Set the names for the X and Y axes.
plt.title(): Adds the main title at the top of the chart.
plt.legend(): Creates the color key box labeled "Zones".
plt.grid(): Turns on the background grid lines.
plt.show(): Opens the window to display the finished graph.
items(): Feeds the zone names and colors into the loop simultaneously.

## Interpretation
Anomalous Stations: Stations S5 and S6 break the general trend line.
The Violation: Generally, higher traffic volumes lead to higher pollution levels (e.g., comparing S8 to S7). However, S5 and S6 maintain the highest pollution levels (PM2.5 above 100) despite only having moderate traffic (45k–50k vehicles). Conversely, S7 has the absolute highest traffic volume (70k vehicles) but maintains a significantly lower PM2.5 level (83).
Explanatory Variable: The zone type variable directly explains this deviation. S5 and S6 are located in an Industrial zone, where factory/manufacturing emissions heavily amplify pollution independently of commuter vehicle traffic.