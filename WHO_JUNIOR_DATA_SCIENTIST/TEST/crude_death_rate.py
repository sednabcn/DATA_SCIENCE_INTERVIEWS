import pandas as pd
death_rate=pd.read_csv("death_rate_.csv",index_col=0)
print(death_rate.shape)

pop_est =pd.read_csv("pop_estimates.csv",index_col=0)

pop_est.loc[17,pop_est.columns[1:3]]=pop_est.loc[17:21,pop_est.columns[1:3]].sum()
pop_est.loc[17,pop_est.columns[0]]="85+"
pop_est=pop_est.drop(index=[18,19,20])

print(pop_est.shape)
scale=100000
crd_top=[]
for ii in range(death_rate.shape[1]-1):
    col=death_rate.columns[ii+1]
    col_=pop_est.columns[ii+1] 
    crd_=death_rate[col].dot(pop_est[col_])/scale
    crd_/=pop_est[col_].sum()
    crd_*=scale
    crd_top.append(round(crd_,1))
print(crd_top)

crude_death=pd.DataFrame(crd_top).T
crude_death.columns=["Crude death rate, United States, 2019", "Crude death rate, Uganda, 2019"]

print(crude_death.head())

"""
┌──(agagora㉿kali)-[~/Desktop/GOAHEAD/PY]
└─$ python3 crude_death_rate.py
(18, 3)
(18, 3)
[42.8, 7.3]
   Crude death rate, United States, 2019  Crude death rate, Uganda, 2019
0                                   42.8                             7.3

"""
