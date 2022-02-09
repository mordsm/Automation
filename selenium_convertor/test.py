from datetime import datetime
from  meteostat import Point, Daily
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

start = datetime(2021, 1, 1)
end = datetime(2021, 12, 31)
oslo = Point(59.9139, 10.7522)
od = Daily(oslo, start, end)
od = od.fetch()
print (od.isnull().sum())
df = od.drop(['snow','wdir','wspd','wpgt','pres','tsun'], axis=1)
df = df.dropna()
print(df)
print(df.isna().sum())
corr = df.corr()
print(corr)
sns.heatmap(corr, cmap="Blues", annot=True)




if not od.empty:
    exit()