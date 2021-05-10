from SIR_model import run
from data_division import before_lockdown_data,lockdown_1_data,lockdown_2_data,lockdown_3_data,lockdown_4_data,unlockdown_1_data
import numpy as np
import pandas as pd
from datetime import timedelta, datetime
from tkinter import *
from chart import create_accuracy,create_images_before,create_images_lockdown1,create_images_lockdown2,create_images_lockdown3,create_images_lockdown4,create_images_unlockdown1
from PIL import Image,ImageTk
from chart import create_error, create_final_chart

'''main solution'''
def solve():
    #getting the data
    predict_range_1=20
    #Running the Model
    #running the model for before lockdown, lockdown 1.0,2.0,3.0,4.0 and unlockdown 1.0 respectively
    #before Lockdown
    #print("Before Lockdown")
    #print('')
    before_lockdown=before_lockdown_data()
    confirmed=before_lockdown.iloc[:,1]
    recovered=before_lockdown.iloc[:,3]
    dead=before_lockdown.iloc[:,2]
    before_lockdown['infected_cases']=before_lockdown['confirmed_cases']-before_lockdown['recovered_cases']-before_lockdown['deaths_cases']
    infected=before_lockdown.iloc[:,4]
    extra_index=before_lockdown.iloc[:,0]
    name='before_lockdown'
    start_date=before_lockdown.iloc[0,0]
    s_0=900000
    i_0=before_lockdown.iloc[0,4]
    r_0=before_lockdown.iloc[0,3]
    predict_range=0
    #before=solve(name, start_date, predict_range, s_0, i_0, r_0, confirmed, recovered, dead, infected, extra_index)
    #before.train()
    run(name, start_date, predict_range, s_0, i_0, r_0, confirmed, recovered, dead, infected, extra_index)

    #Lockdown 1.0
    #print("Lockdown 1.0")
    #print('')
    lockdown_1=lockdown_1_data()
    confirmed=lockdown_1.iloc[:,1]
    recovered=lockdown_1.iloc[:,3]
    dead=lockdown_1.iloc[:,2]
    lockdown_1['infected_cases']=lockdown_1['confirmed_cases']-lockdown_1['recovered_cases']-lockdown_1['deaths_cases']
    infected=lockdown_1.iloc[:,4]
    extra_index=lockdown_1.iloc[:,0]
    name='lockdown_1'
    start_date=lockdown_1.iloc[0,0]
    first=pd.read_csv("prediction_before_lockdown.csv")
    i_0=lockdown_1.iloc[0,4]
    r_0=lockdown_1.iloc[0,3]
    predict_range=0
    #lockdown_10=solve(name, start_date, predict_range, s_0, i_0, r_0, confirmed, recovered, dead, infected, extra_index)
    #lockdown_10.train()
    run(name, start_date, predict_range, s_0, i_0, r_0, confirmed, recovered, dead, infected, extra_index)

    #Lockdown 2.0
    #print("Lockdown 2.0")
    #print('')
    #print('')
    lockdown_2=lockdown_2_data()
    confirmed=lockdown_2.iloc[:,1]
    recovered=lockdown_2.iloc[:,3]
    dead=lockdown_2.iloc[:,2]
    lockdown_2['infected_cases']=lockdown_2['confirmed_cases']-lockdown_2['recovered_cases']-lockdown_2['deaths_cases']
    infected=lockdown_2.iloc[:,4]
    extra_index=lockdown_2.iloc[:,0]
    name='lockdown_2'
    start_date=lockdown_2.iloc[0,0]
    second=pd.read_csv("prediction_lockdown_1.csv")
    #s_0=second.iloc[0,3]
    i_0=lockdown_2.iloc[0,4]
    r_0=lockdown_2.iloc[0,3]
    predict_range=0
    #lockdown_20=solve(name, start_date, predict_range, s_0, i_0, r_0, confirmed, recovered, dead, infected, extra_index)
    #lockdown_20.train()
    run(name, start_date, predict_range, s_0, i_0, r_0, confirmed, recovered, dead, infected, extra_index)

    #Lockdown 3.0
    #print("Lockdown 3.0")
    #print('')
    #print('')
    lockdown_3=lockdown_3_data()
    confirmed=lockdown_3.iloc[:,1]
    recovered=lockdown_3.iloc[:,3]
    dead=lockdown_3.iloc[:,2]
    lockdown_3['infected_cases']=lockdown_3['confirmed_cases']-lockdown_3['recovered_cases']-lockdown_3['deaths_cases']
    infected=lockdown_3.iloc[:,4]
    extra_index=lockdown_3.iloc[:,0]
    name='lockdown_3'
    start_date=lockdown_3.iloc[0,0]
    third=pd.read_csv("prediction_lockdown_2.csv")
    #s_0=third.iloc[0,3]
    i_0=lockdown_3.iloc[0,4]
    r_0=lockdown_3.iloc[0,3]
    predict_range=0
    #lockdown_30=solve(name, start_date, predict_range, s_0, i_0, r_0, confirmed, recovered, dead, infected, extra_index)
    #lockdown_30.train()
    run(name, start_date, predict_range, s_0, i_0, r_0, confirmed, recovered, dead, infected, extra_index)

    #Lockdown 4.0
    #print("Lockdown 4.0")
    #print('')
    #print('')
    lockdown_4=lockdown_4_data()
    confirmed=lockdown_4.iloc[:,1]
    recovered=lockdown_4.iloc[:,3]
    dead=lockdown_4.iloc[:,2]
    lockdown_4['infected_cases']=lockdown_4['confirmed_cases']-lockdown_4['recovered_cases']-lockdown_4['deaths_cases']
    infected=lockdown_4.iloc[:,4]
    extra_index=lockdown_4.iloc[:,0]
    name='lockdown_4'
    start_date=lockdown_4.iloc[0,0]
    fourth=pd.read_csv("prediction_lockdown_3.csv")
    #s_0=fourth.iloc[0,3]
    i_0=lockdown_4.iloc[0,4]
    r_0=lockdown_4.iloc[0,3]
    predict_range=0
    #lockdown_40=solve(name, start_date, predict_range, s_0, i_0, r_0, confirmed, recovered, dead, infected, extra_index)
    #lockdown_40.train()
    run(name, start_date, predict_range, s_0, i_0, r_0, confirmed, recovered, dead, infected, extra_index)

    #UNLockdown 1.0
    #print("Unlockdown 1.0")
    #print('')
    #print('')
    unlockdown_1=unlockdown_1_data()
    confirmed=unlockdown_1.iloc[:,1]
    recovered=unlockdown_1.iloc[:,3]
    dead=unlockdown_1.iloc[:,2]
    unlockdown_1['infected_cases']=unlockdown_1['confirmed_cases']-unlockdown_1['recovered_cases']-unlockdown_1['deaths_cases']
    infected=unlockdown_1.iloc[:,4]
    predict_range=predict_range_1
    len_of_data=len(unlockdown_1)
    last_date=unlockdown_1.iloc[len_of_data-1, 0]
    last_date=last_date+timedelta(days=1)
    extra_index=pd.date_range(start=unlockdown_1.iloc[0,0], periods=(predict_range+len_of_data))
    #extended_index
    name='unlockdown_1'
    start_date=unlockdown_1.iloc[0,0]
    fifth=pd.read_csv("prediction_lockdown_4.csv")
    #s_0=fifth.iloc[0,3]
    i_0=unlockdown_1.iloc[0,4]
    r_0=unlockdown_1.iloc[0,3]
    #unlockdown_30=solve(name, start_date, predict_range, s_0, i_0, r_0, confirmed, recovered, dead, infected, extra_index)
    #unlockdown_30.train()
    run(name, start_date, predict_range, s_0, i_0, r_0, confirmed, recovered, dead, infected, extra_index)


    #getting the actual predicted data
    sixth=pd.read_csv("prediction_unlockdown_1.csv")
    sixth.rename(columns={'Unnamed: 0':'Dates'}, inplace=True)

    #merging the data
    #first holds the before lockdown data
    #second holds the lockdown 1 data
    #third holds the lockdown 2 data
    #fourth holds the lockdown 3 data
    #fifth holds the lockdown 4 data
    #sixth holds the unlockdown 1 data

    merge=pd.concat([first, second], ignore_index=True)
    merge_1=pd.concat([merge, third], ignore_index=True)
    merge_2=pd.concat([merge_1, fourth], ignore_index=True)
    merge_3=pd.concat([merge_2, fifth], ignore_index=True)
    merge_4=pd.concat([merge_3, sixth], ignore_index=True)

    merge_4.to_csv("final_list.csv")
    
    '''main solution end'''

    create_images_before()
    create_images_lockdown1()
    create_images_lockdown2()
    create_images_lockdown3()
    create_images_lockdown4()
    create_images_unlockdown1()
    create_error()
    create_accuracy()
    create_final_chart()

