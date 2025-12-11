""" This script loads the cleaned survey dataset and runs four separate 
OLS regressions, one for each mental health outcome variable 
(Anxiety, Depression, Insomnia, OCD). Summary and results of each regression
are output and saved to a CSV file. """

import pandas as pd
import statsmodels.api as sm

# Load processed data
data = pd.read_csv('data/processed_survey_data.csv')

# Define DataFrame
data_frame = pd.DataFrame(data).dropna()

''' RUN REGRESSIONS 
    Running one regression per mental health variable '''

mental_health_vars = ['Anxiety', 'Depression', 'Insomnia', 'OCD']
all_results = []

for var in mental_health_vars:
    # Define variables
    y = data_frame[var] # Dependent variable
    X = data_frame.drop(columns=mental_health_vars) # Independent variables
    X = sm.add_constant(X)

    # Fit OLS Model
    model = sm.OLS(y,X)
    results = model.fit()

    # Show results
    print("\n", results.summary())

    # Store results in a DataFrame
    reg_results = pd.DataFrame({
        'Dependent': var,
        'Variable': results.params.index,
        'Coefficient': results.params.values,
        'StdErr': results.bse.values,
        'tValue': results.tvalues.values,
        'pValue': results.pvalues.values
    })
    
    all_results.append(reg_results)

# Concatenate all results
final_regression_results = pd.concat(all_results, ignore_index=True)

# Save to CSV
final_regression_results.to_csv('results/music_mental_health_regression_results.csv', index=False)