""" This script performs sentiment analysis on the prepared genre 
    lyrics dataset using the VADER Sentiment Analyzer. Genres are
    deemed on a scale of Weakly Negative to Weakly Positive, and
    results are saved as CSVs for potential future analysis. """

import pandas as pd
import numpy as np

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

''' RUN SENTIMENT ANALYSIS'''
# Sentiment score function
def sentiment_scores(sentence):
    object = SentimentIntensityAnalyzer()
    sentiment_dict = object.polarity_scores(sentence)
    return sentiment_dict['compound']

# Selected genres for sentiment analysis
inputGenres = ['Blues', 'Classical', 'Country', 'Electronic',
               'Folk', 'Jazz', 'Pop_Rock', 'Rap', 'Reggae',
               'Religious', 'RnB', 'Vocal']
genre_sizes = {}
genre_sentiments = {}

# Load each song into vader and calculate average genre sentiment
for genre in inputGenres:
    df = pd.read_csv(f'data/lyric_genre_CSVs/{genre}.csv')
    genre_sizes[genre] = df['word'].size
    average_sentiment = np.array([])
    print(f'Analyzing {genre} genre...')
    # Load each song into vader one by one
    for song in df.itertuples():
        average_sentiment = np.append(average_sentiment, sentiment_scores(song.word))
    genre_sentiments[genre] = [np.mean(average_sentiment)]
    print(f'Average {genre} sentiment: ', genre_sentiments[genre][0],)
    
    if genre_sentiments[genre][0] >= 0.30:
        print(f"Overall {genre} Sentiment: Positive\n")
        genre_sentiments[genre].append(f"Overall {genre} Sentiment: Positive")
    
    elif genre_sentiments[genre][0] >= 0.15 and genre_sentiments[genre][0] < 0.30:
        print(f"Overall {genre} Sentiment: Weakly Positive\n")
        genre_sentiments[genre].append(f"Overall {genre} Sentiment: Weakly Positive")
    
    elif genre_sentiments[genre][0] <= -0.30:
        print(f"Overall {genre} Sentiment: Negative\n")
        genre_sentiments[genre].append(f"Overall {genre} Sentiment: Negative")

    elif genre_sentiments[genre][0] <= -0.15 and genre_sentiments[genre][0] > -0.30:
        print(f"Overall {genre} Sentiment: Weakly Negative\n")
        genre_sentiments[genre].append(f"Overall {genre} Sentiment: Weakly Negative")

    else:
        print(f"Overall {genre} Sentiment: Neutral\n")
        genre_sentiments[genre].append(f"Overall {genre} Sentiment: Neutral")

# Convert sentiment dictionaries into DataFrames
genre_sentiment_averages_df = pd.DataFrame([
    {
        "Genre": genre,
        "Average Sentiment": vals[0],
        "Sentiment Label": vals[1]
    }
    for genre, vals in genre_sentiments.items()
])

genre_sizes_df = pd.DataFrame([
    {
        "Genre": genre,
        "Num Words": size
    }
    for genre, size in genre_sizes.items()
])


print(genre_sentiment_averages_df)
print(genre_sizes_df)

# Save sentiment results to .csv
genre_sentiment_averages_df.to_csv(f'results/genre_sentiment_averages.csv', index=False)
genre_sizes_df.to_csv(f'results/genre_sizes.csv', index=False)

print("\nSentiment analysis records saved successfully!")