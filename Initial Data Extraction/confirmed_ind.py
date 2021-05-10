import pandas as pd
import io
import requests

def confirmed_cases_india():
    #url="https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    confirmed=pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
    confirmed_india=confirmed[confirmed["Country/Region"]=="India"]
    confirmed_india= confirmed_india.drop(['Province/State','Lat','Long'],axis=1)
    confirmed_india= confirmed_india.transpose()
    #print(confirmed_india.columns)
    confirmed_india.rename(columns={131:'confirmed_cases'},inplace=True)
    #print(confirmed_india.columns)
    #print(confirmed_india.index)
    confirmed_india.drop(['Country/Region'], axis=0, inplace=True)
    confirmed_india['Dates']=confirmed_india.index.copy()
    rearrange=['Dates','confirmed_cases']
    confirmed_india=confirmed_india.reindex(columns=rearrange)
    #print(confirmed_india)
    return confirmed_india
