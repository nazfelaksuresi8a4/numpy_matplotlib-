import matplotlib.pyplot as plt
import numpy as np 

def f(x):
    return 1.1*x - 1

xf = 0.1

plt.style.use('dark_background')

fig,ax = plt.subplots(1,1,figsize=(14,2))

ax.set_ylim(-1,1)
ax.set_xlim(-1,1)

line1, = plt.plot([],[])
line2, = plt.plot([],[])

ax.axhline(0,color='black')
ax.axvline(0,color='black')

plt.grid(True,which='major',axis='both')

while True:
    line1.set_xdata(np.linspace(0,1,100))
    line1.set_ydata(np.sin(np.linspace(0,10,100)+xf))

    line2.set_xdata(-np.linspace(0,1,100))
    line2.set_ydata(-np.cos(np.linspace(0,10,100)+xf))

    xf += 0.50
    plt.pause(0.05)

plt.show()
