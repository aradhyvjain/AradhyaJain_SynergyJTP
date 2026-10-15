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
    

