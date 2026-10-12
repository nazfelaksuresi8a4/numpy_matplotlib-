import matplotlib.pyplot as plt 
import numpy as np 

sampling = 10000       #örnekleme hizi
time = 0.04           #zaman

A_ = 1
f_sin = 100            #sinüs dalgasının frekansı
f_tri = 500            #üçgen dalganın frekansı

phi_ = 1               #faz açısı

t_ = np.arange(0, time, 1/sampling)    #zaman dizisi ve 1 / sampling adım

def Vtri(t,f,A):
    return ((2*A) / np.pi) * np.arcsin(np.sin(2*np.pi*f*t))        #taışıyıcı dalga

def Vsin(t,f,A,phi):
    return A * np.sin((2*np.pi*f*t) + phi)                          #sinusiodal dalga

def Pwm(t,Vsinusoidal_,Vtringular_):
    pwm = np.where(Vsinusoidal_>Vtringular_,1,0)                    #iki dalganın karşılaştırılması sonucunda oluşan PWM sinyali (SPWM denir)

    return pwm

Vtringular_ = Vtri(t_,f_tri,A_)
Vsinusoidal_ = Vsin(t_,f_sin,A_,phi_)
Vpwm = Pwm(t_,Vsinusoidal_,Vtringular_)

fig,ax = plt.subplots(3,1)

for i,Vx in zip(range(len(ax)),[Vtringular_,Vsinusoidal_,Vpwm]):
    ax[i].grid(True)
    ax[i].plot(t_,Vx)

plt.show()
