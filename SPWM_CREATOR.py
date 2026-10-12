import matplotlib.pyplot as plt 
import numpy as np 


sampling = 10000       
time = 0.04           

A_ = 1
f_sin = 100            
f_tri = 500   

phi_ = 1               

t_ = np.arange(0, time, 1/sampling)

def Vtri(t,f,A):
    return ((2*A) / np.pi) * np.arcsin(np.sin(2*np.pi*f*t))

def Vsin(t,f,A,phi):
    return A * np.sin((2*np.pi*f*t) + phi)

def Pwm(t,Vsinusoidal_,Vtringular_):
    pwm = np.where(Vsinusoidal_>Vtringular_,1,0)

    return pwm

Vtringular_ = Vtri(t_,f_tri,A_)
Vsinusoidal_ = Vsin(t_,f_sin,A_,phi_)
Vpwm = Pwm(t_,Vsinusoidal_,Vtringular_)

fig,ax = plt.subplots(3,1)

for i,Vx in zip(range(len(ax)),[Vtringular_,Vsinusoidal_,Vpwm]):
    ax[i].grid(True)
    ax[i].plot(t_,Vx)

plt.show()
