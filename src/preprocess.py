""" This script loads the original MXMH survey results dataset from
    Kaggle, cleans it, and prepares it for analysis. The fully processed
    dataset as a CSV file ready for modeling and visualization """

import kagglehub
import pandas as pd
import numpy as np

from kagglehub import KaggleDatasetAdapter

''' LOAD INITIAL DATASET '''
# Set file path
file_path = 'mxmh_survey_results.csv'

# Load the latest version
data = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "catherinerasgaitis/mxmh-survey-results",
  file_path,
  # Provide any additional arguments like
  # sql_query or pandas_kwargs. See the
  # documenation for more information:
  # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
)

# Display initial dataset
print(data.head())

''' DATA PROCESSING AND CLEANING'''
# Drop irrelevant variables
data = data.drop(axis=1, columns=['Primary streaming service', 'Instrumentalist','Composer','Timestamp','Permissions', 'Exploratory', 'Fav genre', 'Foreign languages', 'Music effects'])

# Convert string values to numbers
# Make 'While working' variable binary -- 0 = No, 1 = Yes
data["While working"] = np.where(data["While working"].fillna('').str.contains('Yes'), 1, 0)

# Define mapping where: 0 = Never, 1 = Rarely, 2 = Sometimes, 3 = Very frequently
# Use mapping to make frequency levels numeric
mapping = {'Never': 0, 'Rarely': 1, 'Sometimes': 2, 'Very frequently': 3}
data["Frequency [Classical]"] = data["Frequency [Classical]"].replace(mapping)
data["Frequency [Country]"] = data["Frequency [Country]"].replace(mapping)
data["Frequency [EDM]"] = data["Frequency [EDM]"].replace(mapping)
data["Frequency [Folk]"] = data["Frequency [Folk]"].replace(mapping)
data["Frequency [Gospel]"] = data["Frequency [Gospel]"].replace(mapping)
data["Frequency [Hip hop]"] = data["Frequency [Hip hop]"].replace(mapping)
data["Frequency [Jazz]"] = data["Frequency [Jazz]"].replace(mapping)
data["Frequency [K pop]"] = data["Frequency [K pop]"].replace(mapping)
data["Frequency [Latin]"] = data["Frequency [Latin]"].replace(mapping)
data["Frequency [Lofi]"] = data["Frequency [Lofi]"].replace(mapping)
data["Frequency [Metal]"] = data["Frequency [Metal]"].replace(mapping)
data["Frequency [Pop]"] = data["Frequency [Pop]"].replace(mapping)
data["Frequency [R&B]"] = data["Frequency [R&B]"].replace(mapping)
data["Frequency [Rap]"] = data["Frequency [Rap]"].replace(mapping)
data["Frequency [Rock]"] = data["Frequency [Rock]"].replace(mapping)
data["Frequency [Video game music]"] = data["Frequency [Video game music]"].replace(mapping)

# Display final dataset
print('\n', data.head())

# Save final dataset to .csv
# Save processed data to a .csv
data.to_csv('data/processed_survey_data.csv', index=False)
print(f"\nDataset successfully saved to '{'data/processed_data.csv'}'")