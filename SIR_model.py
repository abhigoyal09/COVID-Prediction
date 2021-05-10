#import loss as loss
import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from datetime import timedelta, datetime

class solve:
    def __init__(self, name, loss, start_date, predict_range,s_0, i_0, r_0, confirmed, recovered, dead, infected, extra_index):
        self.name=name
        self.loss = loss
        self.start_date=start_date
        self.predict_range = predict_range
        self.s_0 = s_0
        self.i_0 = i_0
        self.r_0 = r_0
        self.confirmed=confirmed
        self.recovered=recovered
        self.dead=dead
        self.infected=infected
        self.extra_index=extra_index
                    
    def predict(self, beta, gamma, infected, recovered, death, s_0, i_0, r_0):
        new_index=self.extra_index
        size=len(new_index)
        def SIR(t,y):
            S=y[0]
            I=y[1]
            R=y[2]
            return [-beta*S*I, beta*S*I-gamma*I, gamma*I]
        if self.predict_range==0:
            extended_actual = infected.values
            extended_recovered = recovered.values
            extended_death = death.values
        else:
            extended_actual = np.concatenate((infected.values, [None] * (size - len(infected.values))))
            extended_recovered = np.concatenate((recovered.values, [None] * (size - len(recovered.values))))
            extended_death = np.concatenate((death.values, [None] * (size - len(death.values))))
        return new_index, extended_actual, extended_recovered, extended_death, solve_ivp(SIR, [0, size], [s_0,i_0,r_0], t_eval=np.arange(0, size, 1))
            
    def train(self):
        recovered=self.recovered
        death=self.dead
        infected=self.infected
        name=self.name
        optimal= minimize(loss, [0.00000038, 0.001], args=(infected, recovered, self.s_0, self.i_0, self.r_0), method='L-BFGS-B', bounds=[(0.00000001, 0.4), (0.00000001, 0.4)])
        #print(optimal)
        beta, gamma = optimal.x
        new_index, extended_actual, extended_recovered, extended_death, prediction = self.predict(beta, gamma, infected, recovered, death, self.s_0, self.i_0, self.r_0)
        df = pd.DataFrame({'Infected data': extended_actual, 'Recovered data': extended_recovered, 'Death data': extended_death, 'Susceptible': prediction.y[0], 'Infected': prediction.y[1], 'Recovered': prediction.y[2]}, index=new_index)
        '''fig, ax = plt.subplots(figsize=(15, 10))
        ax.set_title('India')
        df.plot(ax=ax)'''
        #print(f"beta={beta:.8f}, gamma={gamma:.8f}, r_0:{(beta/gamma):.8f}")
        #fig.savefig(f"india_{name}.png")
        df.to_csv(f"prediction_{name}.csv")

def loss(point, infected, recovered, s_0, i_0, r_0):
    size = len(infected)
    beta, gamma = point
    def SIR(t, y):
        S = y[0]
        I = y[1]
        R = y[2]
        return [-beta*S*I, beta*S*I-gamma*I, gamma*I]
    solution = solve_ivp(SIR, [0, size], [s_0,i_0,r_0], t_eval=np.arange(0, size, 1), vectorized=True)
    l1 = np.sqrt(np.mean((solution.y[1] - infected)**2))
    l2 = np.sqrt(np.mean((solution.y[2] - recovered)**2))
    alpha = 0.1
    return alpha * l1 + (1 - alpha) * l2
            

def run(name, start_date, predict_range, s_0, i_0, r_0, confirmed, recovered, dead, infected, extra_index):
    running=solve(name, loss, start_date, predict_range, s_0, i_0, r_0, confirmed, recovered, dead, infected, extra_index)
    running.train()
