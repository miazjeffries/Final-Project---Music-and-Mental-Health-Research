""" This script extracts and processes song lyrics from the MXM SQLite database 
    and merges them with genre information from the MSDGenre text file.  """

import pandas as pd
import sqlite3

# Connect to SQL
connection = sqlite3.connect('data/mxm_dataset.db')

# Get lyrics dataframe
query = 'SELECT * FROM lyrics;'
data_frame = pd.read_sql(query, connection)
data_frame = data_frame.drop(columns=['mxm_tid','count', 'is_test'])

# Show raw lyrics
print(data_frame.head())

# Collapse genre and lyric data
collapsedDF = (data_frame.groupby('track_id')['word'].apply(lambda x: ' '.join(x))).reset_index()
genreDF = pd.read_csv('data/MSDGenre.txt', sep='\t', names=['track_id', 'genre'])
processed_lyrics = pd.merge(collapsedDF, genreDF, on='track_id')

print(processed_lyrics.head())
processed_lyrics.to_csv('data/lyrics/genre.csv', index=False) #make entire genre df

# Make genre based DataFrames
genre_groups = processed_lyrics.groupby('genre')
for genre, df in genre_groups:
    df = df.drop(columns=['genre'])
    filename = f'{genre}.csv'
    df.to_csv(f'data/lyric_genre_CSVs/{genre}.csv', index=False)
