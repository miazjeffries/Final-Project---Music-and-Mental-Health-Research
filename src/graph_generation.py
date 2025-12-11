""" This script generates various visuals using the cleaned
    dataset and saved analyses. Graphs are displayed and saved 
    as PNG files. """

import pandas as pd
import matplotlib.pyplot as plt

# Load processed data
data = pd.read_csv('data/processed_survey_data.csv')

''' PLOT BAR GRAPH #1'''
# Shows average mental health for top listeners across genres
mhBarGraph = pd.DataFrame(columns=("Genre", "Average Anxiety", "Average Depression", "Average Insomnia", "Average OCD"))

for column in data.iloc[:, 4:20].columns:
  mhBarGraph.loc[len(mhBarGraph)] = [column,
      data.loc[data[column] == 3]["Anxiety"].mean(),
      data.loc[data[column] == 3]["Depression"].mean(),
      data.loc[data[column] == 3]["Insomnia"].mean(),
      data.loc[data[column] == 3]["OCD"].mean(),
      ]

print(mhBarGraph.head())

mhBarGraph.plot(figsize=(20, 8), kind="bar")
plt.xticks(mhBarGraph.index, mhBarGraph['Genre'])
plt.xlabel("Genre")
plt.ylabel("Average Mental Health")
plt.title("Average Mental Health For Top Listeners In Each Genre")

# Save figure as .png
#plt.savefig("figures/mental_health_for_top_listeners.png")

''' PLOT BAR GRAPH #2 '''
# Shows average compound mental health across genres
# Compound score: the sum of differences between average of each feature
compBarGraph = pd.DataFrame(columns=("Genre", "Compound Anxiety", "Compound Depression", "Compound Insomnia", "Compound OCD", "Number Of Listeners in Thousands"))

# Calculate overall averages from the original data DataFrame
overall_avg_anxiety = data["Anxiety"].mean()
overall_avg_depression = data["Depression"].mean()
overall_avg_insomnia = data["Insomnia"].mean()
overall_avg_ocd = data["OCD"].mean()

# Iterate through mhBarGraph (which contains average scores per genre) to calculate compound scores
# Assuming mhBarGraph from cell tLlkIxT3lb40 has columns like "Average Anxiety"
for index, row in mhBarGraph.iterrows():
    genre = row["Genre"]
    compound_anxiety = row["Average Anxiety"] - overall_avg_anxiety
    compound_depression = row["Average Depression"] - overall_avg_depression
    compound_insomnia = row["Average Insomnia"] - overall_avg_insomnia
    compound_ocd = row["Average OCD"] - overall_avg_ocd
    number_of_listeners = len(data[data[genre] == 3])/1000

    compBarGraph.loc[len(compBarGraph)] = [
        genre,
        compound_anxiety,
        compound_depression,
        compound_insomnia,
        compound_ocd,
        number_of_listeners,
    ]

print(compBarGraph.head())
compBarGraph.plot(figsize=(20, 8), kind="bar")
plt.xticks(mhBarGraph.index, mhBarGraph['Genre'])
plt.xlabel("Genre")
plt.ylabel("Average Compound Mental Health")
plt.title("Compound Scores for Each Genre")

# Save figure as .png
#plt.savefig("figures/compound_mental_health_across_genres.png")


''' PlOT BAR GRAPH #3 '''
# Mapping to convert sentiment genres to survey genres names
mapping = {'Classical': 'Frequency [Classical]', 
           'Country': 'Frequency [Country]', 
           'Electronic': 'Frequency [EDM]',
           'Folk': 'requency [Folk]',
           'Jazz': 'Frequency [Jazz]',
           'Pop_Rock': 'Frequency [Pop]',
           'Rap': 'Frequency [Hip hop]',
           'Religious': 'Frequency [Gospel]',
           'RnB': 'Frequency [R&B]',
           }

# Load sentiment data and merge with compound DataFrame
comp_sent_df = pd.read_csv('results/genre_sentiment_averages.csv')
comp_sent_df = comp_sent_df.drop(columns=('Sentiment Label'))
comp_sent_df = comp_sent_df.replace(mapping)
compBarGraph = pd.merge(compBarGraph, comp_sent_df, on='Genre')

# Plot compound scores with sentiment
compBarGraph.plot(figsize=(20, 8), kind='bar')
plt.xticks(compBarGraph.index, compBarGraph['Genre'])
plt.xlabel('Genre')
plt.ylabel('Average Compound Mental Health And Sentiment')
plt.title('Compound Scores for Each Genre With Sentiment')

# Save combined compound/sentiment graph
plt.savefig("figures/compound_sentiment_graph.png")

plt.show()