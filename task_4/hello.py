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


