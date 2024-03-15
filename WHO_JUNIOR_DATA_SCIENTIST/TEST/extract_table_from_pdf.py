# Extract table from PDFS age_st.pdf (Publication) and dataexe01.pdf (Table provide for this exercise)

import pandas as pd
import camelot

Path='/home/agagora/Desktop/GOAHEAD/JUNIOR-DATASET/age_st.pdf'
Path1='/home/agagora/Desktop/GOAHEAD/JUNIOR-DATASET/dataexe01.pdf'

def extract_table_from_pdf(path,page_number:int,flavor:str="stream",stdout:bool=True):
           import camelot
           return camelot.read_pdf(path,flavor="stream",suppress_stdout=True,
                        pages="all")[page_number].df 

camelot_df = extract_table_from_pdf(Path,9)


age_st_cols=["Age group","Segi (“world”) standard","Scandinavian (“European”) standard", "WHO World Standard*"]
age_st=pd.DataFrame(camelot_df.loc[2:19,:].values,index=range(18),columns=age_st_cols)


print(age_st.head(18))
age_st.to_csv("age_st.csv")

camelot_df = extract_table_from_pdf(Path1,3)

death_rate_cols=["Age group (years)" ,"Death rate, United States, 2019","Death rate, Uganda, 2019"]
death_rate=pd.DataFrame(camelot_df.loc[2:19,:].values,index=range(18),columns=death_rate_cols)

death_rate.to_csv("death_rate_.csv")

print(death_rate.head(18))

"""
┌──(agagora㉿kali)-[~/Desktop/GOAHEAD/PY]
└─$ python3  extract_table_from_pdf.py
            0                        1                                                  2                    3
0                                       Table 1. Standard Population Distribution (per...                     
1   Age group  Segi (“world”) standard                 Scandinavian (“European”) standard  WHO World Standard*
2         0-4                    12.00                                               8.00                 8.86
3         5-9                    10.00                                               7.00                 8.69
4       10-14                     9.00                                               7.00                 8.60
5       15-19                     9.00                                               7.00                 8.47
6       20-24                     8.00                                               7.00                 8.22
7       25-29                     8.00                                               7.00                 7.93
8       30-34                     6.00                                               7.00                 7.61
9       35-39                     6.00                                               7.00                 7.15
10      40-44                     6.00                                               7.00                 6.59
11      45-49                     6.00                                               7.00                 6.04
12      50-54                     5.00                                               7.00                 5.37
13      55-59                     4.00                                               6.00                 4.55
14      60-64                     4.00                                               5.00                 3.72
15      65-69                     3.00                                               4.00                 2.96
16      70-74                     2.00                                               3.00                 2.21
17      75-79                     1.00                                               2.00                 1.52
18      80-84                     0.50                                               1.00                 0.91
19        85+                     0.50                                               1.00                 0.63
RangeIndex(start=0, stop=4, step=1)
                    0                                1                                                  2
0                                                       Data analysis exercise: Our World in Data Juni...
1   Age group (years)  Death rate, United States, 2019                           Death rate, Uganda, 2019
2                 0-4                             0.04                                               0.40
3                 5-9                             0.02                                               0.17
4               10-14                             0.02                                               0.07
5               15-19                             0.02                                               0.23
6               20-24                             0.06                                               0.38
7               25-29                             0.11                                               0.40
8               30-34                             0.29                                               0.75
9               35-39                             0.56                                               1.11
10              40-44                             1.42                                               2.04
11              45-49                             4.00                                               5.51
12              50-54                            14.13                                              13.26
13              55-59                            37.22                                              33.25
14              60-64                            66.48                                              69.62
15              65-69                           108.66                                             120.78
16              70-74                           213.10                                             229.88
17              75-79                           333.06                                             341.06
18              80-84                           491.10                                             529.31
19                85+                           894.45                                             710.40
RangeIndex(start=0, stop=3, step=1)
"""
