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