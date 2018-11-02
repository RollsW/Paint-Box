import matplotlib.colors as mplc



colormap =  mplc.LinearSegmentedColormap.from_list("map",[mplc.hex2color("#011c41"),
                                                          mplc.hex2color("#F2E8C3"),
                                                          mplc.hex2color("#F5A219"),
                                                          mplc.hex2color("#F27612"),
                                                          mplc.hex2color("#DA2A04")])



import numpy as np
import matplotlib.pyplot as plt


n = 10000

x = np.random.randint(0,100,n)
y = np.random.randint(0,100,n)
t = np.random.randint(0,100,n)
plt.scatter(x,y,c=x,cmap=colormap)



plt.show()
