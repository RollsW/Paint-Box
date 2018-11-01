import matplotlib.colors as mplc

l = ['#800000','#730000','#660000','#590000','#4C0000','#3F0000','#320000','#250000','#180000','#0B0000','#000000','#800000','#8D1A1A','#9A3434','#A74E4E','#B46868','#C18282','#CE9C9C','#DBB6B6','#E8D0D0','#F5EAEA','#FFFFFF','#DB6E00','#C56300','#AF5800','#994D00','#834200','#6D3700','#572C00','#412100','#2B1600','#150B00','#000000','#DB6E00','#DF7D1A','#E38C34','#E79B4E','#EBAA68','#EFB982','#F3C89C','#F7D7B6','#FBE6D0','#FFF5EA','#FFFFFF']



#colormap =  mplc.LinearSegmentedColormap.from_list("map",[mplc.hex2color("#193441"),
##                                                          mplc.hex2color("#3F5866"),
#                                                          mplc.hex2color("#B1BEC0")
#                                                                         ])
#

for i in l:
    x = mplc.hex2color(i)
    for j in x:
        print(int(255*j), end="\t")
    print(i)

#import numpy as np
#import matplotlib.pyplot as plt
#
#
#n = 10000
#
#x = np.random.randint(0,100,n)
#y = np.random.randint(0,100,n)
#t = np.random.randint(0,100,n)
#plt.scatter(x,y,c=0-y**2,cmap=colormap)
#
#
#
#plt.show()
