import pandas as pd
data = [['Sona','Kirakosyan','female','20-30','student'], ['Liana','Varosyan','female','20-30','student'], ['Artur','Mkrtchyan','male','20-30','student'],
        ['Ruzanna','Ordyan','female','50-60','student'],['Nairi','Hakobyan','male','20-30','tutor'], ['Jora','Karyan','male','20-30','student'],
         ['Hayk','Sahakyan','male','20-30','student'],['Anahit','Kirakosyan','female','30-40','student'], ['Salbina','Alaverdyan','female','20-30','student'],
        ['Tatev','Alaverdyan','female','20-30','student'],['Vlad','Harutyunyan','male','20-30','student']]
columns = ['name', 'surname', 'sex', 'age group', 'status']

df=pd.DataFrame(data = data, columns = columns)
print(df)