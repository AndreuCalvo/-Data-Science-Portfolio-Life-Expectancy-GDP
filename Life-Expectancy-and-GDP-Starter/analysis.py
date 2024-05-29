import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Load the data
data_path_file =  r"G:\Mi unidad\Estudis\Data science\CodeAcademy\Portfoli\Life Expectancy and GDP\Life-Expectancy-and-GDP-Starter\all_data.csv"
life_expectancy_data = pd.read_csv(data_path_file)
#Check the dataset, explore and explain data
print(life_expectancy_data.head())
print(life_expectancy_data.info())
print(life_expectancy_data.describe())
#Change the names of the variables
life_expectancy_data_rename = life_expectancy_data.rename(columns={'Country': 'country', 'Year': 'year', 'Life expectancy at birth (years)': 'leab', 'GDP': 'gdp'})
#Obtain the list of the all differents coutries in the data
#print(life_expectancy_data['country'].unique())
countries = life_expectancy_data_rename['country'].unique()
#Segment data for country
chile_data = life_expectancy_data_rename[life_expectancy_data_rename.country == 'Chile']
china_data = life_expectancy_data_rename[life_expectancy_data_rename.country == 'China']
germany_data = life_expectancy_data_rename[life_expectancy_data_rename.country == 'Germany']
mexico_data = life_expectancy_data_rename[life_expectancy_data_rename.country == 'Mexico']
usa_data = life_expectancy_data_rename[life_expectancy_data_rename.country == 'United States of America']
zimbabwe_data = life_expectancy_data_rename[life_expectancy_data_rename.country == 'Zimbabwe']
#Analize any country data
plt.subplot(1,2,1)
sns.boxplot(x='country', y='leab', data= life_expectancy_data_rename)
plt.subplot(1,2,2)
sns.boxplot(x='country', y='gdp', data = life_expectancy_data_rename)
plt.show()
plt.clf()

#Correlation between leab and GDP
#CHILE
plt.subplot(2,3,1)
sns.stripplot(x = 'leab', y= 'gdp', data = chile_data)
plt.title('CHILE correlation leab/gdp')
#CHINA
plt.subplot(2,3,2)
sns.stripplot(x = 'leab', y= 'gdp', data = china_data)
plt.title('CHINA correlation leab/gdp')
#GERNANY
plt.subplot(2,3,3)
sns.stripplot(x = 'leab', y= 'gdp', data = germany_data)
plt.title('GERMANY correlation leab/gdp')
#MEXICO
plt.subplot(2,3,4)
sns.stripplot(x = 'leab', y= 'gdp', data = mexico_data)
plt.title('MEXICO correlation leab/gdp')
#USA
plt.subplot(2,3,5)
sns.stripplot(x = 'leab', y= 'gdp', data = usa_data)
plt.title('USA correlation leab/gdp')
#ZIMBABWE
plt.subplot(2,3,6)
sns.stripplot(x = 'leab', y= 'gdp', data = zimbabwe_data)
plt.title('GERMANY correlation leab/gdp')

plt.show()
plt.clf()
#All the coutries have a positive correlation between this two variables (leab and gdp), this correlation has all the sense because show us 
# the relation between the money and the life expectancy. In zimbabwe exist some anomalie correlation. We decide to study in more detail this data

#ZIMBABWE 
plt.subplot(1,2,1)
sns.pointplot(x ='year', y='leab', data = zimbabwe_data)
plt.subplot(1,2,2)
sns.pointplot(x ='year', y='gdp', data = zimbabwe_data)
plt.show()
plt.clf()
# This two plots show as how zimbabwe suffers some economical crisis during the 2004, the country doesn't recover since 2008 


#Ditribution  leab
#CHILE
plt.subplot(2,3,1)
sns.countplot(x = 'leab', data = chile_data)
plt.title('CHILE correlation leab/gdp')
#CHINA
plt.subplot(2,3,2)
sns.countplot(x = 'leab', data = china_data)
plt.title('CHINA correlation leab/gdp')
#GERNANY
plt.subplot(2,3,3)
sns.countplot(x = 'leab', data = germany_data)
plt.title('GERMANY correlation leab/gdp')
#MEXICO
plt.subplot(2,3,4)
sns.countplot(x = 'leab', data = mexico_data)
plt.title('MEXICO correlation leab/gdp')
#USA
plt.subplot(2,3,5)
sns.countplot(x = 'leab', data = usa_data)
plt.title('USA correlation leab/gdp')
#ZIMBABWE
plt.subplot(2,3,6)
sns.countplot(x = 'leab', data = zimbabwe_data)
plt.title('GERMANY correlation leab/gdp')
plt.show()
plt.clf()
# This dataset doesn't have enough data to create a histograms where we can check the real distribution about the leab variable


