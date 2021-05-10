import pandas as pd

def recovered_cases_india():
    recovered=pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv")
    recovered_india=recovered[recovered["Country/Region"]=="India"]
    recovered_india= recovered_india.drop(['Province/State','Lat','Long'],axis=1)
    recovered_india= recovered_india.transpose()
    #print(recovered_india.columns)
    recovered_india.rename(columns={125:'recovered_cases'},inplace=True)
    #print(recovered_india.columns)
    #print(recovered_india.index)
    recovered_india.drop(['Country/Region'], axis=0, inplace=True)
    recovered_india['Dates']=recovered_india.index.copy()
    rearrange=['Dates','recovered_cases']
    recovered_india=recovered_india.reindex(columns=rearrange)
    #print(recovered_india)
    return recovered_india
