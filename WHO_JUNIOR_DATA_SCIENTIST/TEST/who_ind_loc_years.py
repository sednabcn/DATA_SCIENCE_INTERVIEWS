#Returning population estimates of United States and Uganda (1950-2021) based on the 5-year-age groups and sex  

import pandas as pd
import requests
import json

# Define a function that will take a relative path as an input, call the API, and return a dataframe
def callAPI(relative_path:str, topic_list:bool = False) -> pd.DataFrame:

    base_url = "https://population.un.org/dataportalapi/api/v1" 

    target = base_url + relative_path # Query string parameters may be appended here or directly in the provided relative path
    # Calls the API
    response = requests.get(target)

    # Reformats response into a JSON object
    j = response.json()

    # The block below will deal with paginated results.
    # If results not paginated, this will be skipped.
    try:
    # If results are paginated, they are transformed into a python dictionary.
    # The data may be accessed using the 'data' key of the dictionary.
        df = pd.json_normalize(j['data'])
        # As long as the nextPage key of the dictionary contains an address for the next API call, the function will continue to call the API and append the results to the dataframe.
        while j['nextPage'] is not None:
                response = requests.get(j['nextPage'])
                j = response.json()
                df_temp = pd.json_normalize(j['data'])
                df = df._append(df_temp)
    except:
           if topic_list:
                df = pd.json_normalize(j, 'indicators')
           else:
                df = pd.DataFrame(j)
    return(df)
# Define a function that order a DataFrame by the column with range ['a-b']
def data_range_sort(data:pd.DataFrame(), index_col,reverse:bool=False):
                  def tt(x):
                      for ch in ['-','+']:
                          if ch in x:
                              return int(x.replace(ch,' ').split()[0])
                  newd=[(ii,tt(y)) for ii,y in enumerate(data[data.columns[index_col]])]
                  newd.sort(key=lambda x:x[1],reverse=reverse)
                  new_order=[item[0] for item in newd]
                  return data.loc[new_order,:]
# Uses callAPI function to get a list of parameters of Population Estimates(1950-2021) in the locations : United States and Uganda

df_ily = callAPI("/data/indicators/46/locations/800,840/start/1950/end/2021")

# Extract he values of population with the variant "Median" acording the indicator Id=46 :Population by 5-year age groups and sex 
# Get the values of population estimates of Uganda (1950-2021) based on the 5-year-age groups and sex 

UGA_pop=df_ily.loc[df_ily["locationId"]==800][["ageLabel","value"]].groupby("ageLabel").sum().reset_index()

#print(UGA_pop.head(10))
# Get the values of population estimates of Uganda (1950-2021) based on the 5-year-age groups and sex 
USA_pop=df_ily.loc[df_ily["locationId"]==840][["ageLabel","value"]].groupby("ageLabel").sum().reset_index()

#print(USA_pop.head(10))
# Build a table concatenating these dataframes: USA_pop and UGA_pop
pop_estimates=pd.concat([USA_pop,UGA_pop],axis=1)

# Drop duplicate columns "ageLabel"
pop_estimates=pop_estimates.T.drop_duplicates().T

#Sort the DataFrame by the columns "ageLabel"
pop_estimates=data_range_sort(pop_estimates,0)

# Rename the columns of pop_estimates with the columns:["Age group(years)","United States,1950-2021","Uganda,1950-2021"])                              
pop_estimates.columns=["Age group(years)","United States,1950-2021","Uganda,1950-2021"]
pop_estimates=pop_estimates.reset_index(drop=True)
print(pop_estimates)
pop_estimates.to_csv("pop_estimates.csv")


"""
                                                                                 
┌──(agagora㉿kali)-[~/Desktop/GOAHEAD/PY]
└─$ python3  who_ind_loc_years.py
   Age group(years) United States,1950-2021 Uganda,1950-2021
0               0-4            2665210640.0      519693594.0
10              5-9            2668027455.0      430624776.0
1             10-14            2679617305.0      364621694.0
3             15-19            2641486119.0      304857173.0
4             20-24            2577774727.0      247983694.0
5             25-29            2545208491.0      196924943.0
6             30-34            2503870046.0      154941831.0
7             35-39            2414993437.0      122755538.0
8             40-44            2310941145.0       98369926.0
9             45-49            2179233684.0       78607475.0
11            50-54            2031594854.0       61767003.0
12            55-59            1846346004.0       47654243.0
13            60-64            1607991820.0       35805208.0
14            65-69            1363344713.0       25540584.0
15            70-74            1074644842.0       16577941.0
16            75-79             791310710.0        9379062.0
17            80-84             516180293.0        4328277.0
18            85-89             280311477.0        1447730.0
19            90-94             109315002.0         309845.0
20            95-99              26921208.0          33614.0
2              100+               3917208.0           2974.0
                                              
"""
"""
# Identifies ID code for Western Africa
western_africa_id = df_locations.loc[df_locations["name"]=="Western Africa", "id"].iloc[0]

# Restricts the dataframe to only include geographies from Western Africa
df_locations = df_locations[df_locations['id']==western_africa_id]

# Stores country codes in a list
country_codes = [str(code) for code in df_locations["id"].values]

# Converts country code list into a string to be used in later API call
country_selection_string = ",".join(country_codes)

# Uses callAPI function to get a list of Family Planning indicators
df_topics = callAPI("/topics/", topic_list=True)

# Stores indicator codes in a list
indicator_codes = [str(code) for code in df_topics["id"].values]

# Converts indicator code list into string to be used in later API call
indicator_selection_string = ",".join(indicator_codes)

# Calls the API to return the indicator values for the selected indicators and countries.
df = callAPI(f"/data/indicators/{indicator_selection_string}/locations/{country_selection_string}/start/2020/end/2020")

# Finally, filters the returned results to only include median values for All Women, and limits the number of columns retained in the new dataframe.
df2 = df.loc[(df['variant']=="Median") & (df['category']=="All women"), ['location', "indicator", "variant","category","value"]]
"""




