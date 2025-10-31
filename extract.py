import pandas as pd

data = {
     'ID': [101,102,103],
     'Name':['Ram','Raj','Rakesh'],
     'Age':[29,34,42]
}
df=pd.DataFrame(data)
print(df)