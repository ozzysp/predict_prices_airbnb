import pandas as pd
import pathlib
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor
from sklearn.model_selection import train_test_splitls


months = {'jan': 1, 'fev': 2, 'mar': 3, 'abr': 4, 'mai': 5, 'jun': 6,
          'jul': 7, 'ago': 8, 'set': 9, 'out': 10, 'nov': 11, 'dez': 12}

path_bases = pathlib.Path('dataset')

base_airbnb = pd.DataFrame()

for file in path_bases.iterdir():
    name_month = file.name[:3]
    month = months[name_month]

    year = file.name[-8:]
    year = int(year.replace('.csv', ''))

    df = pd.read_csv(path_bases / file.name, low_memory=False)
    df['year'] = year
    df['month'] = month
    base_airbnb = base_airbnb.append(df)

display(base_airbnb)
