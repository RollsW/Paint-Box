import matplotlib.colors as mplc

l = ['#011C41','#01193A','#011633','#01132C','#011025','#010D1E','#010A17','#010710','#010409','#010102','#000000','#011C41','#1A3354','#334A67','#4C617A','#65788D','#7E8FA0','#97A6B3','#B0BDC6','#C9D4D9','#E2EBEC','#FFFFFF','#F2E8C3','#DAD1AF','#C2BA9B','#AAA387','#928C73','#7A755F','#625E4B','#4A4737','#323023','#1A190F','#000000','#F2E8C3','#F3EAC9','#F4ECCF','#F5EED5','#F6F0DB','#F7F2E1','#F8F4E7','#F9F6ED','#FAF8F3','#FBFAF9','#FFFFFF','#F5A219','#DC9216','#C38213','#AA7210','#91620D','#78520A','#5F4207','#463204','#2D2201','#141200','#000000','#F5A219','#F6AB30','#F7B447','#F8BD5E','#F9C675','#FACF8C','#FBD8A3','#FCE1BA','#FDEAD1','#FEF3E8','#FFFFFF','#F27612','#DA6A10','#C25E0E','#AA520C','#92460A','#7A3A08','#622E06','#4A2204','#321602','#1A0A00','#000000','#F27612','#F3842A','#F49242','#F5A05A','#F6AE72','#F7BC8A','#F8CAA2','#F9D8BA','#FAE6D2','#FBF4EA','#FFFFFF','#DA2A04','#C42604','#AE2204','#981E04','#821A04','#6C1604','#561204','#400E04','#2A0A04','#140604','#000000','#DA2A04','#DE3F1D','#E25436','#E6694F','#EA7E68','#EE9381','#F2A89A','#F6BDB3','#FAD2CC','#FEE7E5','#FFFFFF']



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
