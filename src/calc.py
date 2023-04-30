from dataParser import settings
import pandas as pd # type: ignore

def calc(data: pd.DataFrame, settings: settings) -> list[list[pd.DataFrame]]:   
    output: list[list[pd.DataFrame]] = [[], []]
    stateGroup = data.groupby('state')
    calcs = stateGroup.aggregate({'new_case':settings.operations, 'new_death':settings.operations})
    data['submission_date'] = pd.to_datetime(data['submission_date'], format='%m/%d/%Y')
    data.sort_values(by='submission_date', inplace=True)
    data.reset_index(drop=True)
    for state in data['state'].unique():
        df_dict = {}
        for op in settings.operations:
            df_dict[op] = [calcs.loc[state, 'new_case'][op], calcs.loc[state, 'new_death'][op]]
        df1 = pd.DataFrame(df_dict, index=['new_case', 'new_death'])
        df1 = df1.round(2)
        df1.Name = f'{state} calculated'
        output[1].append(df1)
        df2: pd.DataFrame = data.loc[data['state'] == state]
        df2.sort_values(by=['submission_date'])
        df2.Name = f'{state} over time'
        output[0].append(df2)
    return output
