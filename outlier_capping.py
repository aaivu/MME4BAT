# -*- coding: utf-8 -*-
"""outlier_capping.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZJ1U75p2YP1xNbO92pnkB0TnWsmYG0VJ
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime,date
from google.colab import files

from google.colab import drive
drive.mount('/content/drive')

path= '/content/drive/Shareddrives/MSc - Shiveswarran/Processed data/Nine_months_data/bus_stop_times_feature_added_all.csv'

df = pd.read_csv(path)

df

df.columns

df = df.drop(df[df['dwell_time_in_seconds'] > 600].index )

df = df.loc[(df['time_of_day']>=6) & (df['time_of_day']<19)]

df1 = df[df['direction']==1]

sns.set(style='whitegrid')
sns.set(rc={'figure.figsize':(16,12)})
sns.boxplot(x='bus_stop', y='dwell_time_in_seconds', data =  df1)

def condition(x):
  if x == 101:
    return 'pro'
  if x == 102:
    return 'mod'
  if x == 103:
    return 'mod'
  if x == 104:
    return 'br'
  if x == 105:
    return 'pro'
  if x == 106:
    return 'mod'
  if x == 107:
    return 'br'
  if x == 108:
    return 'br'
  if x == 109:
    return 'pro'
  if x == 110:
    return 'mod'
  if x == 111:
    return 'br'
  if x == 112:
    return 'br'
  if x == 113:
    return 'mod'
  if x == 114:
    return 'br'
  else:
    return 'br'

df1['stop_type'] = df1['bus_stop'].apply(condition)

sns.set(style='whitegrid')
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.boxplot(x='stop_type', y='dwell_time_in_seconds', data =  stop_times)

cap = {'br':300,'mod':420, 'pro':540}

df1.rename(columns = {'dwell_time_in_seconds':'dwell_time_in_seconds_old'}, inplace = True)

df1

df1['dwell_time_in_seconds'] = ''

stop_times = pd.DataFrame()

for name, group in df1.groupby('stop_type'):
  cap_value = cap[name]
  print(cap_value)
  group['dwell_time_in_seconds'] =  list(map(lambda x: cap_value if x > cap_value else x  , (group['dwell_time_in_seconds_old'])))
  stop_times= stop_times.append(group)

stop_times

type(cap_value)

stop_times['dwell_time_in_seconds'].equals(stop_times['dwell_time_in_seconds_old'])

stop_times = stop_times.sort_values(['trip_id', 'bus_stop'])

stop_times

def download_csv(data,filename):
  filename= filename + '.csv'
  data.to_csv(filename, encoding = 'utf-8-sig',index= False)
  files.download(filename)

download_csv(stop_times,'bus_stop_times_feature_added_all')