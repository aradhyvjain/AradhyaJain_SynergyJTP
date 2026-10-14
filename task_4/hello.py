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
print("The unique genres are", df['genre'].unique())
print("\n")
print("Top 3 songs by streams are\n",df.loc[df['streams_k'].nlargest(3).index,'song'])
print("\nPopular songs and frequently skipped songs")
print(df[(df['streams_k']>400)&(df['skip_pct']>25)])
