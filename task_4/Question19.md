# Question-19 Does Practice really drive skill?
## Aim
Plot a scatter chart of hours against rating and highlight the player with 20 hours in a different color. Use Pandas to compute the correlation twice: once with all ten players and once without the 20-hour player. Interpret: does the data support the coach’s claim for typical players?

## Code
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
players = pd.DataFrame({'hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 20],
                        'rating': [50, 56, 48, 55, 52, 57, 49, 54, 51, 95]})
print(players)
correlation_allplayers=players['hours'].corr(players['rating'])
typical_players=players[players['hours']!=20]
correlation_typical=typical_players['hours'].corr(typical_players['rating'])
print(correlation_allplayers,correlation_typical)
plt.scatter(typical_players['hours'], typical_players['rating'],color='blue',label='Typical Players', s=100)#s is for size
outlier=players[players['hours']==20]
plt.scatter(outlier['hours'], outlier['rating'], color='red',label ="Outlier")
plt.title("Ratings Vs Number of hours")
plt.xlabel=("Practice Hours per week")
plt.ylabel("Skill Rating")
plt.grid()
plt.legend(loc='best')
plt.show()
```

## Output
```
(image in figures section)
   hours  rating
0      1      50
1      2      56
2      3      48
3      4      55
4      5      52
5      6      57
6      7      49
7      8      54
8      9      51
9     20      95
0.8599438484105459 0.02847473987257497
```

## Explanation
Data Creation: Builds a pandas DataFrame (players) with hours (1 through 9, plus 20) and corresponding rating values.
Correlation with Outlier: Computes the Pearson correlation coefficient (correlation_allplayers) across all 10 data points.
Filtering: Creates a subset (typical_players) that excludes the outlier where hours != 20.
Correlation without Outlier: Computes the correlation coefficient (correlation_typical) for the remaining typical players.
Visualization: Plots a scatter graph with typical players in blue and the single outlier in red, labeled with a title and grid.

## Interpretation
No, the data does not support the coach's claim.
While the full dataset shows a strong positive correlation (\(\approx 0.86\)), this relationship is completely driven by a single extreme outlier (the 20-hour player with a 95 rating). When this individual is removed, the correlation drops to nearly zero (\(\approx 0.03\)), showing that there is no meaningful linear relationship between practice hours and skill level among the typical players.