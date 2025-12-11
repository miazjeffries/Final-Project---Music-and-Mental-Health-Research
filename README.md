
PROJECT TITLE: 
    Music and Mental Health Research

PURPOSE OF PROJECT: 
    The purpose of this project is to investigate and analyze the connection between music listening habits and mental health. We use a self reported survey to collect listeners anxiety, depression, insomnia, and OCD scores on a scale from 1 to 10, and compare them to their self reported music listening habits. We also look at a dataset of songs lyrics, math them with genre, and perform sentiment analysis per genre. We then analyze sentiment against mental health to find a connection between positive sentiment and better health and vice versa. 

VERSION or DATE:
    December 10, 2025

USER INSTRUCTIONS:
    1. Clone the repository to your local machine
    2. Install required libraries using 'pip install -r requirements.txt'
    3. To process original survey dataset, run ‘preprocess.py’
    4. To run mental health regressions with processed survey data, run ‘regression_analysis.py’
    5. To process lyric data into genre categories, run ‘lyric_processing.py’
    6. To run lyric sentiment analysis using VADER, run ‘sentiment_analysis.py’
    7. To generate graphs for survey and sentiment analysis data, run ‘graph_generation.py’
    8. All data, figures, and results are saved to their respective directories. 

AUTHORS:
    Mia Jeffries
    Max Sindel-Dempcy
    Marvin Romero

NOTES:
    '/src' contains all python files needed to create results
    '/data' contains datasets and modified/generated data
    '/figures' contains generated graphs
    '/results' contains generated analysis metrics