import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np

'''HEATMAP 2D ARRAY İSTER'''

sns.heatmap(np.random.normal(0,9000,(10,10)),
            vmin=0.3,
            vmax=0.9,
            cmap=plt.colormaps()[6],
            center=0.5,
            robust=False,
            fmt='.2g')
plt.show()
