# Question-3 Spotify Song
## Aim
To create a dataframeand print its shapte and dtypes and number of unique genres and to find popular but frequently skipped songs

## Code
```python
import numpy as np
import pandas as pd
#creating the dataframe
songs = {'song': ['Neon Drive', 'Monsoon Loop', 'Gravity', 'Night Bus', 'Cherry Static', 'Dust Roads', 'Run It Back', 'Paper Moon'],
         'genre': ['Pop', 'LoFi', 'Rock', 'LoFi', 'Pop', 'Folk', 'HipHop', 'Folk'],
         'streams_k': [520, 310, 450, 280, 610, 150, 390, 205],
         'skip_pct': [18, 9, 32, 12, 41, 7, 27, 10],
         'duration_sec': [201, 245, 289, 198, 176, 310, 187, 262]}
df=pd.DataFrame(songs)
print(df)
print("\n")
print("The shape of the dataframe is",df.shape)
print(df.dtypes)
print("\n")
print("The unique genres are",len(df['genre'].unique()))
print("\n")
print("Top 3 songs by streams are\n",df.loc[df['streams_k'].nlargest(3).index,'song'])
print("\nPopular songs and frequently skipped songs")
print(df[(df['streams_k']>400)&(df['skip_pct']>25)])
```

# Output
```text
            song   genre  streams_k  skip_pct  duration_sec
0     Neon Drive     Pop        520        18           201
1   Monsoon Loop    LoFi        310         9           245
2        Gravity    Rock        450        32           289
3      Night Bus    LoFi        280        12           198
4  Cherry Static     Pop        610        41           176
5     Dust Roads    Folk        150         7           310
6    Run It Back  HipHop        390        27           187
7     Paper Moon    Folk        205        10           262


The shape of the dataframe is (8, 5)
song            object
genre           object
streams_k        int64
skip_pct         int64
duration_sec     int64
dtype: object


The number of unique genres are 5


Top 3 songs by streams are
 4    Cherry Static
0       Neon Drive
2          Gravity
Name: song, dtype: object

Popular songs and frequently skipped songs
            song genre  streams_k  skip_pct  duration_sec
2        Gravity  Rock        450        32           289
4  Cherry Static   Pop        610        41           176
```

# Explanation
df["name of the column"].unique() is used to display the unique values of the column in the form of the list. df["Name of the column"].nlargest(quantity) returns the top 3 values of the column and .index is used to return the index of those values.

# Interpretation
if the platform recommends songs using stream count only then as per the data there are many songs with high stream count and high skip rate as well. Therefor the suggestion system will be fundamentally flawed. The suggestion system of an application should be based on  high stream count andlow skip rate.