import pandas as pd

def deaths_cases_india():
    death=pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")
    deaths_india=death[death["Country/Region"]=="India"]
    deaths_india= deaths_india.drop(['Province/State','Lat','Long'],axis=1)
    deaths_india= deaths_india.transpose()
    #print(deaths_india.columns)
    deaths_india.rename(columns={131:'deaths_cases'},inplace=True)
    #print(deaths_india.columns)
    #print(deaths_india.index)
    deaths_india.drop(['Country/Region'], axis=0, inplace=True)
    deaths_india['Dates']=deaths_india.index.copy()
    rearrange=['Dates','deaths_cases']
    deaths_india=deaths_india.reindex(columns=rearrange)
    #print(deaths_india)
    return deaths_india
