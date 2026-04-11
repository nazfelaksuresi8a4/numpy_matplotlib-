import matplotlib.pyplot as plt 
import numpy as np

r = 6
n = 100

fig,ax = plt.subplots(1,1)


def f(Fn):
	global ax
	
	for nX in range(Fn+1):
		t = np.linspace(0,nX/10,nX)

		x = r * np.sin(t)
		y = r * np.cos(t)
		
		ax.clear()
		ax.plot(x,y)
		
		plt.pause(0.05)
		
f(n)
plt.show()		