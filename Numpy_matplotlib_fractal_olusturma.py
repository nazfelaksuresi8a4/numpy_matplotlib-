#Fraktal oluşturucu

#renk skalası üreticisi
#sadece 10' un katlarını destekler
import numpy as np 
import matplotlib.pyplot as plt
import math

def r(x,qN,divf):
    return (np.sin(np.linspace(0,10,(100 * x) // divf * qN)**2) * (np.cos(np.linspace(0,10,(100 * x) // divf * qN)**2))) #sinX^2 * cosX^2 = nX

divF = 2
nDİV = 100
nQ = 50
qN = 10

o1 = r(nQ,qN,divF)

rDİV = len(o1) // nDİV
reshaped1 = o1.reshape(len(o1) // rDİV ,rDİV)

plt.style.use('dark_background')
plt.grid(True,which='minor',axis='both')
plt.axhline(0,color='red')
plt.axvline(0,color='green')
plt.imshow(reshaped1)
plt.show()




#bu kod r(x,qN,divf) fonksiyonu içersinde trigonometrik fonksiyonları kullanarak bir fraktal oluşturur 
