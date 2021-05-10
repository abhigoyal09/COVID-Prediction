import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def create_error():
    final_csv=pd.read_csv("final_list.csv")
    final_csv=final_csv.drop(columns=['Death data','Susceptible','Unnamed: 0'])
    final_csv['Percentage_error_infected']=None
    final_csv['Percentage_error_recovered']=None
    i=0
    while(final_csv.iloc[i,1]!=np.NaN):
        if(final_csv.iloc[i,1]!=0):
            final_csv.iloc[i,5]=((final_csv.iloc[i,1]-final_csv.iloc[i,3])/final_csv.iloc[i,1])*100
        if(final_csv.iloc[i,2]!=0):
            final_csv.iloc[i,6]=((final_csv.iloc[i,2]-final_csv.iloc[i,4])/final_csv.iloc[i,2])*100
        if i==len(final_csv)-1:
            break
        i=i+1
    final_csv=final_csv.drop(columns=['Infected data','Infected','Recovered data','Recovered'])
    final_csv['Dates']=pd.to_datetime(final_csv['Dates'], errors='coerce')
    final_csv=final_csv[final_csv['Dates']>'2020-04-19']
    #fig,ax=plt.subplots(figsize=(15,10))
    final_csv.plot(x='Dates').get_figure()
    plt.xlabel("Dates")
    plt.ylabel('Percentage Error')
    plt.title('Error Rate')
    name=7
    plt.savefig(f'prediction_{name}.png')

def create_accuracy():
    final_csv=pd.read_csv("final_list.csv")
    final_csv=final_csv.drop(columns=['Death data','Susceptible','Unnamed: 0'])
    final_csv['Percentage_accuracy_infected']=None
    final_csv['Percentage_accuracy_recovered']=None
    i=0
    while(final_csv.iloc[i,1]!=np.NaN):
        if(final_csv.iloc[i,1]!=0):
            final_csv.iloc[i,5]=100-abs((final_csv.iloc[i,1]-final_csv.iloc[i,3])/final_csv.iloc[i,1])*100
        if(final_csv.iloc[i,2]!=0):
            final_csv.iloc[i,6]=100-abs((final_csv.iloc[i,2]-final_csv.iloc[i,4])/final_csv.iloc[i,2])*100
        if i==len(final_csv)-1:
            break
        i=i+1
    final_csv=final_csv.drop(columns=['Infected data','Infected','Recovered data','Recovered'])
    final_csv['Dates']=pd.to_datetime(final_csv['Dates'], errors='coerce')
    final_csv=final_csv[final_csv['Dates']>'2020-04-19']
    #fig,ax=plt.subplots(figsize=(15,10))
    final_csv.plot(x='Dates').get_figure()
    plt.xlabel("Dates")
    plt.ylabel('Percentage Accuracy')
    plt.title('Accuracy Rate')
    name=8
    plt.savefig(f'prediction_{name}.png')
    
def create_images_before():
    starting=pd.read_csv('prediction_before_lockdown.csv')
    starting=starting.drop(columns=['Death data','Susceptible'])
    starting['Dates']=pd.to_datetime(starting['Dates'], errors='coerce')
    starting.plot(x='Dates').get_figure()
    plt.xlabel("Dates")
    plt.ylabel('No. of cases')
    plt.title('Before Lockdown')
    name=1
    plt.savefig(f'prediction_{name}.png')

def create_images_lockdown1():
    starting=pd.read_csv('prediction_lockdown_1.csv')
    starting=starting.drop(columns=['Death data','Susceptible'])
    starting['Dates']=pd.to_datetime(starting['Dates'], errors='coerce')
    starting.plot(x='Dates').get_figure()
    plt.xlabel("Dates")
    plt.ylabel('No. of cases')
    plt.title('Lockdown 1.0')
    name=2
    plt.savefig(f'prediction_{name}.png')
    
def create_images_lockdown2():
    starting=pd.read_csv('prediction_lockdown_2.csv')
    starting=starting.drop(columns=['Death data','Susceptible'])
    starting['Dates']=pd.to_datetime(starting['Dates'], errors='coerce')
    starting.plot(x='Dates').get_figure()
    plt.xlabel("Dates")
    plt.ylabel('No. of cases')
    plt.title('Lockdown 2.0')
    name=3
    plt.savefig(f'prediction_{name}.png')    

def create_images_lockdown3():
    starting=pd.read_csv('prediction_lockdown_3.csv')
    starting=starting.drop(columns=['Death data','Susceptible'])
    starting['Dates']=pd.to_datetime(starting['Dates'], errors='coerce')
    starting.plot(x='Dates').get_figure()
    plt.xlabel("Dates")
    plt.ylabel('No. of cases')
    plt.title('Lockdown 3.0')
    name=4
    plt.savefig(f'prediction_{name}.png')

def create_images_lockdown4():
    starting=pd.read_csv('prediction_lockdown_4.csv')
    starting=starting.drop(columns=['Death data','Susceptible'])
    starting['Dates']=pd.to_datetime(starting['Dates'], errors='coerce')
    starting.plot(x='Dates').get_figure()
    plt.xlabel("Dates")
    plt.ylabel('No. of cases')
    plt.title('Lockdown 4.0')
    name=5
    plt.savefig(f'prediction_{name}.png')

def create_images_unlockdown1():
    starting=pd.read_csv('prediction_unlockdown_1.csv')
    starting.rename(columns={'Unnamed: 0':'Dates'}, inplace=True)
    starting=starting.drop(columns=['Death data','Susceptible'])
    starting['Dates']=pd.to_datetime(starting['Dates'], errors='coerce')
    starting.plot(x='Dates').get_figure()
    plt.xlabel("Dates")
    plt.ylabel('No. of cases')
    plt.title('Unlockdown 1.0')
    name=6
    plt.savefig(f'prediction_{name}.png')
    
def create_final_chart():
    final=pd.read_csv('final_list.csv')
    final=final.drop(columns=['Death data','Susceptible','Unnamed: 0'])
    final['Dates']=pd.to_datetime(final['Dates'], errors='coerce')
    final.plot(x='Dates').get_figure()
    plt.xlabel("Dates")
    plt.ylabel('No. of cases')
    plt.title('Covid India')
    name=9
    plt.savefig(f'prediction_{name}.png')
