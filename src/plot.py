from dataParser import settings
import matplotlib.pyplot as plt # type: ignore
import matplotlib.axes as axes # type: ignore
import pandas as pd # type: ignore
import numpy as np # type: ignore

def plot(data: list[list[pd.DataFrame]], settings: settings) -> None:
    plt1: axes._axes.Axes
    plt2: axes._axes.Axes
    plt3: axes._axes.Axes
    plt4: axes._axes.Axes

    fig, ((plt1, plt2), (plt3, plt4)) = plt.subplots(2, 2)

    series = []
    for df in data[1]:
        series.append([df.Name.split(' ')[0], df.loc['new_case', 'mean']])
    top10: pd.DataFrame = pd.DataFrame(series)
    top10 = top10.sort_values(1, ascending=False).reset_index(drop=True)
    top10 = top10.iloc[:10]
    top10 = top10.iloc[::-1].reset_index(drop=True)

    # Plot 1

    for df in data[0]:
        if(df.Name.split(' ')[0] in top10[0].unique()):
            plt1.plot(df['submission_date'], df['new_case'], label=df.Name.split(' ')[0])
    plt1.set_xlabel('Date')
    plt1.set_ylabel('New Cases')
    plt1.legend()
    plt1.set_title('Number of New Cases (10 Highest)')

    # Plot 2

    for df in data[0]:
        if(df.Name.split(' ')[0] in top10[0].unique()):
            plt2.plot(df['submission_date'], df['new_death'], label=df.Name.split(' ')[0])
    plt2.set_xlabel('Date')
    plt2.set_ylabel('New Deaths')
    plt2.set_title('Number of New Deaths (10 Highest)')
    plt2.legend()

    # Plot 3

    def label(pct):
        return f'{np.round(pct, 2)} %'

    plt3.pie(top10[1].to_list(), labels=top10[0].to_list(), autopct=lambda pct: label(pct))
    plt3.set_title('Average New Case Per Day (10 Highest)')
    plt3.legend(['{0} - {1:1.2f}'.format(i,j) for i,j in zip(top10[0].to_list(), top10[1].to_list())], loc='lower left', bbox_to_anchor=(-0.5, 0))

    # Plot 4

    top30: pd.DataFrame = pd.DataFrame(series)
    top30 = top30.sort_values(1, ascending=False).reset_index(drop=True)
    top30 = top30.iloc[:30]
    top30 = top30.iloc[::-1].reset_index(drop=True)

    histData = []

    for df in data[0]:
        if(df.Name.split(' ')[0] in top30[0].unique()):
            for i in range(df.iloc[[-1], df.columns.get_loc('tot_death')].values[0]):
                histData.append(df.Name.split(' ')[0])

    plt4.hist(histData, len(data[0]), ec='k')
    plt4.set_title('Total Deaths per State (30 Highest)')

    for i in range(len(data[1])):
        print('----------------------------------------------')
        print('\t\t' + data[1][i].Name.split(' ')[0])
        print('----------------------------------------------')
        print(data[1][i])

    if(settings.enabledPlots):
        plt.show()

    return
