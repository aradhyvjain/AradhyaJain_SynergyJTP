# Question-13 The Catalog Gap
## Aim
To merge the tables with an inner, a left and an outer join, and record the row count of each. to report listing of every catalog track, including tracks that have never been played.

## Code
```python
import numpy as np
import pandas as pd
tracks = pd.DataFrame({'track_id': [1, 2, 3, 4],
                       'title': ['Neon Drive', 'Gravity', 'Night Bus', 'Dust Roads'],
                       'artist': ['Aria', 'Vega', 'Aria', 'Mohan']})
plays = pd.DataFrame({'track_id': [1, 2, 3, 5], 'plays': [520, 450, 280, 90]})
catalog=pd.merge(tracks,plays, on='track_id', how='left')
catalog['plays']=catalog['plays'].fillna(0)
print(catalog)
```

## Output
```text
   track_id       title artist  plays
0         1  Neon Drive   Aria  520.0
1         2     Gravity   Vega  450.0
2         3   Night Bus   Aria  280.0
3         4  Dust Roads  Mohan    0.0
```

## Explanation
pd.merge() is used to combine two dataframes together based on a shared column.
on='track_id': specifies the common column used to look up matching rows in both tables.
how='left'specifies a left join. it ensusres that every single row from the first table (Tracks) is kept, even if there is no matching record found in the second table (plays).
.fillna(0) is used to replace np.nan values by 0.


## Interpretation
The presence of track_id 5 in the plays table but not in the tracks table indicates a data inconsistency. It tells us that users are playing a track that does not exist in the official catalog.
Which join type hides it: A Left Join or an Inner Join will hide this row, as neither will include keys that are exclusively in the right table.






























