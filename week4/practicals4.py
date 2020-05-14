# Exercise#1
import pandas as pd
import numpy as np
data = [['Sona','Kirakosyan','female','20-30','student'], ['Liana','Varosyan','female','20-30','student'], ['Artur','Mkrtchyan','male','20-30','student'],
        ['Ruzanna','Ordyan','female','50-60','student'],['Nairi','Hakobyan','male','20-30','tutor'], ['Jora','Karyan','male','20-30','student'],
         ['Hayk','Sahakyan','male','20-30','student'],['Anahit','Kirakosyan','female','30-40','student'], ['Salbina','Alaverdyan','female','20-30','student'],
        ['Tatev','Alaverdyan','female','20-30','student'],['Vlad','Harutyunyan','male','20-30','student']]
columns = ['name', 'surname', 'sex', 'age group', 'status']

df=pd.DataFrame(data = data, columns = columns)
df.index = np.arange(1, len(df) + 1)
print(df)

# Exercise#2
import pandas as pd
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 15)
df = pd.read_csv('netflix_titles.csv')

filtered=df[~(df['cast'].isnull()) & (df['release_year']>=2015)&((df['cast'].str.contains('Kevin Spacey'))|(df['cast'].str.contains('Leonardo DiCaprio')))]
print(len(filtered. show_id))

# Exercise#3
import pandas as pd
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 15)
df = pd.read_csv('netflix_titles.csv')

number=df.groupby(['director']).count()['show_id']
final=pd.merge(df,number,on='director')
print(final)

# Exercise#4
import pandas as pd
import numpy as np

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 15)
df = pd.read_csv('netflix_titles.csv')
new_df = df.assign(cast=df.cast.str.split(',')).explode('cast')
new_df.index = np.arange(1, len(new_df) + 1)
print(new_df)

# Exercise#5
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 15)

df = pd.read_csv('netflix_titles.csv', parse_dates = ['date_added'])
filtered=df[~(df['cast'].isnull()) & ((df['cast'].str.contains('Antonio Banderas')))]
ds = filtered.sort_values(by='date_added')
ds['duration'] = ds['duration'].str.replace('min', '')
ds['duration'] = ds['duration'].str.replace('1 Season', '200')
ds['duration'] = pd.to_numeric(ds['duration'])
plt.plot(ds['date_added'], ds['duration'], label='line')
plt.show()

# Exercise#6
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 15)

df = pd.read_csv('netflix_titles.csv', parse_dates = ['date_added'])
filtered=df[~(df['date_added'].isnull())]
ds = filtered.sort_values(by='date_added')
ds.groupby(['date_added']).count()
ds['date_added'] = ds['date_added'].dt.strftime('%Y %B-%d')
plt.xticks(rotation=90)
plt.plot(ds['date_added'], ds['show_id'], label='line')
ds.plot(x='date_added', y='show_id', kind='bar', legend=False)
plt.show()

# Exercise#7
import pandas as pd

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 15)

df = pd.read_csv('netflix_titles.csv', parse_dates = ['date_added'])
filtered=df[~(df['date_added'].isnull())]
ds = filtered.sort_values(by='date_added')
ds["difference"] = ds["date_added"].diff(1)

print(ds)
