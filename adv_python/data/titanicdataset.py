import pandas as pd
import numpy as np
df=pd.read_csv("..//data/tested.csv")
print(df.shape)
df.drop(['Cabin'],axis=1,inplace=True)
df.fillna(method='ffill',inplace=True)
print(df['Embarked'])
print(pd.crosstab(index=df['Sex'],columns=df['Embarked']))
print(df.isna().sum())
print(df.groupby(['Sex','Embarked'])['Embarked'].count)
print(pd.pivot_table(df,index=['Sex','Age'],aggfunc=np.sum))
print(df.sort_values(by=['Pclass','Age'],ascending=True))
df['Survived']=df['Survived'].apply(lambda val:'Yes' if val==1 else 'No')
print(df)