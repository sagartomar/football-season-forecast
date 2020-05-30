import os
import pandas as pd

def load_data(fpath: str):
    if os.path.isfile(fpath):
        return pd.read_csv(fpath)
    raise Exception('File not found')

def prepare_data(df: pd.DataFrame, team_categorical: pd.core.arrays.categorical.Categorical=None):
    df = df.loc[:, ['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']]
    df.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'}, inplace=True)
    if team_categorical is None:
        team_categorical = pd.Categorical(df.HomeTeam)
    df['HomeTeamId'] = pd.Categorical(df.HomeTeam, dtype=team_categorical.dtype).codes
    df['AwayTeamId'] = pd.Categorical(df.AwayTeam, dtype=team_categorical.dtype).codes
    return df, team_categorical
