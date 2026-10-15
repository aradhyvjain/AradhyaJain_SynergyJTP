# Question-9 Player efficiency
## Aim
To add columns using vectorised operations and to add such columns whose values are derived from the values of the other columns.

## Code
```python
import numpy as np
import pandas as pd
players = pd.DataFrame({'player': ['A', 'B', 'C', 'D', 'E', 'F'],
                        'score': [4200, 1800, 7600, 3100, 5900, 900],
                        'minutes': [30, 45, 60, 20, 40, 15]})
#adding a new column
players["score_per_min"]=players["score"]/players['minutes']
#creating a function to add the tier column
def addTier(x):
    if x>=6000:
        return "Elite"
    elif ((x>=3000) and (x<6000)):
        return "Skilled"
    else:
        return "Rookie"
players['Tier']=players['score'].apply(addTier)
#to add bonus column
bonus_map={"Elite":500, "Skilled":200,"Rookie":50}
players['bonus']=players['Tier'].map(bonus_map)
total_bonus=players['bonus'].sum()
print(players)
print("Total bonus points are", total_bonus)
```

## Output
```text
  player  score  minutes  score_per_min     Tier  bonus
0      A   4200       30     140.000000  Skilled    200
1      B   1800       45      40.000000   Rookie     50
2      C   7600       60     126.666667    Elite    500
3      D   3100       20     155.000000  Skilled    200
4      E   5900       40     147.500000  Skilled    200
5      F    900       15      60.000000   Rookie     50
Total bonus points are 1200
```

## Explanation
map function is used when you want to transform or replace individual values in a single column
applu() function is used when you want to apply a function to an entire series or to rows or columns of a DataFrame


## Interpretation
No the top scorer is not the most efficient player as his score per min is less than 2 of 0the other players.

