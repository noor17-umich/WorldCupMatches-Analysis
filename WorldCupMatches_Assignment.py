
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joypy as jp
from seaborn_qqplot import pplot

# Q1: Load the WorldCupMatches.csv into a DataFrame
df = pd.read_csv('WorldCupMatches.csv')

# Q2: Draw density curves to show the distributions of Home Team Goals for every year.
sns.displot(df, x='Home Team Goals', hue='Year', kind='kde', fill=True)
plt.title("Density of Home Team Goals per Year")
plt.show()

# Q3: Draw violin plots to summarize Home Team Goals distributions for each year
plt.figure(figsize=(12, 6))
ax = sns.violinplot(data=df, x='Year', y='Home Team Goals')

# Labels for years ending in 0
labels = [str(year) if year % 10 == 0 else "" for year in df['Year'].unique()]
ax.set_xticklabels(labels)
plt.title("Violin Plot of Home Team Goals by Year")
plt.show()

# Q4: Visualize distributions for Home Team Goals and Away Team Goals with Joypy
plt.style.use('seaborn-white')
data = df[['Year', 'Home Team Goals', 'Away Team Goals']]
jp.joyplot(data.groupby('Year')['Home Team Goals'].apply(list).values(), labels=df['Year'].unique())
jp.joyplot(data.groupby('Year')['Away Team Goals'].apply(list).values(), labels=df['Year'].unique())
plt.legend(labels=['Home Team Goals', 'Away Team Goals'])
plt.show()

# Q5: Group data by Home Team Initials and plot the sum of Home Team Goals for the top 5 countries
home_goals = df.groupby('Home Team Initials')['Home Team Goals'].sum().reset_index()
top_countries = home_goals.sort_values(by='Home Team Goals', ascending=False).head(5)
plt.figure(figsize=(10, 6))
sns.barplot(data=top_countries, x='Home Team Initials', y='Home Team Goals')
plt.title("Top 5 Countries by Home Team Goals")
plt.show()

# Q6: Joyplot for densities of Home Team Goals and Away Team Goals for top 4 countries
top_4_countries = home_goals.head(4)['Home Team Initials'].values
top_4_data = df[df['Home Team Initials'].isin(top_4_countries)]
plt.style.use('dark_background')
jp.joyplot(top_4_data.groupby('Home Team Initials')['Home Team Goals'].apply(list).values(), labels=top_4_countries)
jp.joyplot(top_4_data.groupby('Home Team Initials')['Away Team Goals'].apply(list).values(), labels=top_4_countries)
plt.legend(labels=['Home Team Goals', 'Away Team Goals'])
plt.show()

# Q7: Draw a QQ plot to compare Home Team Goals and Away Team Goals
plt.style.use('ggplot')
pplot(df['Home Team Goals'], df['Away Team Goals'])
plt.title("QQ Plot Comparing Home Team Goals and Away Team Goals")
plt.show()

