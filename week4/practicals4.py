import pandas as pd
data = [['Sona','Kirakosyan','female','20-30','student'], ['Liana','Varosyan','female','20-30','student'], ['Artur','Mkrtchyan','male','20-30','student'],
        ['Ruzanna','Ordyan','female','50-60','student'],['Nairi','Hakobyan','male','20-30','tutor'], ['Jora','Karyan','male','20-30','student'],
         ['Hayk','Sahakyan','male','20-30','student'],['Anahit','Kirakosyan','female','30-40','student'], ['Salbina','Alaverdyan','female','20-30','student'],
        ['Tatev','Alaverdyan','female','20-30','student'],['Vlad','Harutyunyan','male','20-30','student']]
columns = ['name', 'surname', 'sex', 'age group', 'status']

df=pd.DataFrame(data = data, columns = columns)
print(df)

import pandas as pd
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 15)
df = pd.read_csv('netflix_titles.csv')

filtered=df[~(df['cast'].isnull()) & (df['release_year']>=2015)&((df['cast'].str.contains('Kevin Spacey'))|(df['cast'].str.contains('Leonardo DiCaprio')))]

print(len(filtered. columns))


import pandas as pd
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 15)
df = pd.read_csv('netflix_titles.csv')

number=df.groupby(['director']).count()['show_id']
final=pd.merge(df,number,on='director')

print(final)
