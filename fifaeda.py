#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np 
import seaborn as sns
from matplotlib import pyplot as plt


fifa=pd.read_csv("C:\\Users\\ashish\\Documents\\Python DS project\\fifaeda\\fifa data.csv")


fifa.head

fifa.info()


fifa.shape


fifa.describe(include='all')

fifa.head()


for col in fifa.columns:
    print(col)

fifa['nationality'].value_counts()


fifa['nationality'].value_counts()[0:15]


fifa['nationality'].value_counts()[0:15].keys()


plt.figure(figsize=(10,8))
plt.bar(list(fifa['nationality'].value_counts()[0:5].keys()),list(fifa['nationality'].value_counts()[0:5]))
plt.show

player_salary = fifa[['short_name','wage_eur']]
player_salary.head()


player_salary=player_salary.sort_values(by=['wage_eur'],ascending=False)


player_salary.head


player_salary.head()

plt.figure(figsize=(10,8))


plt.figure(figsize=(10,8))
plt.bar(list(player_salary['short_name'])[0:10],list(player_salary['wage_eur'])[0:10],color='r')
plt.show()

fifa['nationality']=='Germany'

Germany=fifa[fifa['nationality']=='Germany']
Germany.head()


Germany.sort_values(by=['height_cm'],ascending=False)


Germany.sort_values(by=['height_cm'],ascending=False).head()


Germany.sort_values(by=['wage_eur'],ascending=False).head()

Germany.sort_values(by=['weight_kg'],ascending=False).head()


Germany[['short_name','wage_eur']].sort_values(by=['short_name'],ascending=False)


player_shooting = fifa[['short_name','shooting']]


player_shooting.sort_values(by=['short_name'],ascending=False)

player_defending = fifa[['short_name','defending','nationality','club']]

player_defending.sort_values(by=['short_name'],ascending=False)


player_defending.sort_values(by=['defending'],ascending=False).head()


real_madrid=fifa[fifa['club']=='Real Madrid']
real_madrid.sort_values(by=['wage_eur'],ascending=False).head()


real_madrid.sort_values(by=['shooting'],ascending=False).head(10)


real_madrid.sort_values(by=['defending'],ascending=False).head(10)


real_madrid['nationality'].value_counts()




