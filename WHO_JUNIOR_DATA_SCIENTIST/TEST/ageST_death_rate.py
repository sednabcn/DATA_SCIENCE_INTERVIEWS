import pandas as pd
death_rate=pd.read_csv("death_rate_.csv",index_col=0)
print(death_rate.shape)

# age standardized population distribution
age_est =pd.read_csv("age_st.csv",index_col=0)

#print(age_est.shape)
scale=100000
crd_top=[]
for ii in range(death_rate.shape[1]-1):
    crd_top_=[]
    for jj in range(age_est.shape[1]-1):
        col=death_rate.columns[ii+1]
        col_=age_est.columns[jj+1] 
        crd_=death_rate[col].dot(age_est[col_])/scale
        crd_/=age_est[col_].sum()
        crd_*=scale
        crd_top_.append(round(crd_,1))
    crd_top.append(crd_top_)
#print(crd_top)

asdr=pd.DataFrame(crd_top)
asdr.columns=age_est.columns[1:]
asdr.index=["United States","Uganda"]

print(asdr.head())
"""
──(agagora㉿kali)-[~/Desktop/GOAHEAD/PY]
└─$ python3 ageST_death_rate.py
(18, 3)
(18, 4)
[[23.0, 38.3, 28.4], [23.3, 38.1, 28.7]]
               Segi (“world”) standard  Scandinavian (“European”) standard  WHO World Standard*
United States                     23.0                                38.3                 28.4
Uganda                            23.3                                38.1                 28.7

"""
