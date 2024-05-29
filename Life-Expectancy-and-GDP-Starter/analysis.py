import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import seaborn as sns

data_path_file =  r"G:\Mi unidad\Estudis\Data science\CodeAcademy\Portfoli\Life Expectancy and GDP\Life-Expectancy-and-GDP-Starter\all_data.csv"
life_expectancy_data = pd.read_csv(data_path_file)
print(life_expectancy_data.head())
print(life_expectancy_data.info())
print(life_expectancy_data.describe())
print(life_expectancy_data['Country'].unique())