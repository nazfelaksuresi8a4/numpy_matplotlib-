import matplotlib.pyplot as plt 
import numpy as np 


sampling = 10000       
time = 0.04           

A_ = 1
f_sin = 100            
f_tri = 500   

phi_ = 1               

t_ = np.arange(0, time, 1/sampling) #zaman dizisi

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

fig,ax = plt.subplots(4,1)
Nax = len(ax)

for i,Vx in zip(range(len(ax)),[Vtringular_,Vsinusoidal_,Vpwm,0]):
    if i > Nax-2:
        ax[3].plot(Vsinusoidal_)
        ax[3].plot(Vpwm)

    else:
        ax[i].plot(t_,Vx)

    ax[i].grid(True)

plt.show()
