import pandas as pd
import numpy as np
from confirmed_ind import confirmed_cases_india
from deaths_ind import deaths_cases_india
from recovered_ind import recovered_cases_india
from datetime import datetime

def before_lockdown_data():
    confirmed_india=confirmed_cases_india()
    deaths_india=deaths_cases_india()
    recovered_india=recovered_cases_india()
    india_cases=confirmed_india.merge(deaths_india, on='Dates')
    india_cases=india_cases.merge(recovered_india, on='Dates')
    india_cases=india_cases.astype({'Dates':'datetime64'})
    india_cases=india_cases.astype({'confirmed_cases':'int'})
    india_cases=india_cases.astype({'deaths_cases':'int'})
    india_cases=india_cases.astype({'recovered_cases':'int'})
    india_cases=india_cases[india_cases.confirmed_cases!=0]
    india_cases=india_cases.reset_index(drop=True)
    #selecting before lockdown data
    india_cases=india_cases[india_cases.Dates<='2020-03-24']
    india_cases=india_cases.reset_index(drop=True)
    return india_cases

def lockdown_1_data():
    confirmed_india=confirmed_cases_india()
    deaths_india=deaths_cases_india()
    recovered_india=recovered_cases_india()
    india_cases=confirmed_india.merge(deaths_india, on='Dates')
    india_cases=india_cases.merge(recovered_india, on='Dates')
    india_cases=india_cases.astype({'Dates':'datetime64'})
    india_cases=india_cases.astype({'confirmed_cases':'int'})
    india_cases=india_cases.astype({'deaths_cases':'int'})
    india_cases=india_cases.astype({'recovered_cases':'int'})
    india_cases=india_cases[india_cases.confirmed_cases!=0]
    india_cases=india_cases.reset_index(drop=True)
    #selecting before lockdown data
    india_cases=india_cases[india_cases.Dates>='2020-03-25']
    india_cases=india_cases[india_cases.Dates<='2020-04-14']
    india_cases=india_cases.reset_index(drop=True)
    return india_cases

def lockdown_2_data():
    confirmed_india=confirmed_cases_india()
    deaths_india=deaths_cases_india()
    recovered_india=recovered_cases_india()
    india_cases=confirmed_india.merge(deaths_india, on='Dates')
    india_cases=india_cases.merge(recovered_india, on='Dates')
    india_cases=india_cases.astype({'Dates':'datetime64'})
    india_cases=india_cases.astype({'confirmed_cases':'int'})
    india_cases=india_cases.astype({'deaths_cases':'int'})
    india_cases=india_cases.astype({'recovered_cases':'int'})
    india_cases=india_cases[india_cases.confirmed_cases!=0]
    india_cases=india_cases.reset_index(drop=True)
    #selecting before lockdown data
    india_cases=india_cases[india_cases.Dates>='2020-04-15']
    india_cases=india_cases[india_cases.Dates<='2020-05-03']
    india_cases=india_cases.reset_index(drop=True)
    return india_cases

def lockdown_3_data():
    confirmed_india=confirmed_cases_india()
    deaths_india=deaths_cases_india()
    recovered_india=recovered_cases_india()
    india_cases=confirmed_india.merge(deaths_india, on='Dates')
    india_cases=india_cases.merge(recovered_india, on='Dates')
    india_cases=india_cases.astype({'Dates':'datetime64'})
    india_cases=india_cases.astype({'confirmed_cases':'int'})
    india_cases=india_cases.astype({'deaths_cases':'int'})
    india_cases=india_cases.astype({'recovered_cases':'int'})
    india_cases=india_cases[india_cases.confirmed_cases!=0]
    india_cases=india_cases.reset_index(drop=True)
    #selecting before lockdown data
    india_cases=india_cases[india_cases.Dates>='2020-05-04']
    india_cases=india_cases[india_cases.Dates<='2020-05-17']
    india_cases=india_cases.reset_index(drop=True)
    return india_cases

def lockdown_4_data():
    confirmed_india=confirmed_cases_india()
    deaths_india=deaths_cases_india()
    recovered_india=recovered_cases_india()
    india_cases=confirmed_india.merge(deaths_india, on='Dates')
    india_cases=india_cases.merge(recovered_india, on='Dates')
    india_cases=india_cases.astype({'Dates':'datetime64'})
    india_cases=india_cases.astype({'confirmed_cases':'int'})
    india_cases=india_cases.astype({'deaths_cases':'int'})
    india_cases=india_cases.astype({'recovered_cases':'int'})
    india_cases=india_cases[india_cases.confirmed_cases!=0]
    india_cases=india_cases.reset_index(drop=True)
    #selecting before lockdown data
    india_cases=india_cases[india_cases.Dates>='2020-05-18']
    india_cases=india_cases[india_cases.Dates<='2020-05-31']
    india_cases=india_cases.reset_index(drop=True)
    return india_cases

def unlockdown_1_data():
    confirmed_india=confirmed_cases_india()
    deaths_india=deaths_cases_india()
    recovered_india=recovered_cases_india()
    india_cases=confirmed_india.merge(deaths_india, on='Dates')
    india_cases=india_cases.merge(recovered_india, on='Dates')
    india_cases=india_cases.astype({'Dates':'datetime64'})
    india_cases=india_cases.astype({'confirmed_cases':'int'})
    india_cases=india_cases.astype({'deaths_cases':'int'})
    india_cases=india_cases.astype({'recovered_cases':'int'})
    india_cases=india_cases[india_cases.confirmed_cases!=0]
    india_cases=india_cases.reset_index(drop=True)
    #selecting before lockdown data
    india_cases=india_cases[india_cases.Dates>='2020-06-01']
    india_cases=india_cases.reset_index(drop=True)
    return india_cases
