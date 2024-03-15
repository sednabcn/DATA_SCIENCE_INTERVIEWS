import pandas as pd
def data_range_sort(data:pd.DataFrame(), index_col:int,reverse:bool=False):
                  def tt(x):
                      for ch in ['-','+']:
                          if ch in x:
                              return int(x.replace(ch,' ').split()[0])
                  newd=[(ii,tt(y)) for ii,y in enumerate(data[data.columns[index_col]])]
                  newd.sort(key=lambda x:x[1],reverse=reverse)
                  new_order=[item[0] for item in newd]
                  return data.loc[new_order,:]

dg=[['a', 'b', 'c', 'd'], ['0-4', 0, 1, 5], ['100+', 2, 3, 4], ['85-89', 3, 1, 5], ['5-9', 4, 5, 6], ['75-79', 5, 5, 7], ['35-39', 3, 6, 7], ['10-14', 6, 2, 5]]

df=pd.DataFrame(dg[1:], columns=dg[0])

df_=data_range_sort(df,0)
print(df_)
df_1=data_range_sort(df,0,reverse=True)
print(df_1)                        
