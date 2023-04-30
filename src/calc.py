from dataParser import settings
import pandas as pd # type: ignore
import numpy as np
# INPUT: 
# - The raw data from the website stored in a dataframe.
# - The settings taken from settings.json
# OUTPUT:
# - An array of at least 4 dataframes to be plotted after calculations.

def calc(data: pd.DataFrame) -> list[pd.DataFrame]:   
    data = data[['submission_date', 'new_case', 'new_death']]

    stat = pd.DataFrame({
        'mean': [data['new_case'].mean(), data['new_death'].mean()],
        'median': [data['new_case'].median(), data['new_death'].median()],
        'variance': [data['new_case'].var(), data['new_death'].var()],
        'standard deviation': [data['new_case'].std(), data['new_death'].std()]
    }, index=['new_case', 'new_death'])

    output = pd.DataFrame({'statistics': stat.index})
    for col in stat.columns:
        output[col] = stat[col].values
    output.set_index('statistics', inplace= True)
    output= output.round(2)
    return output
