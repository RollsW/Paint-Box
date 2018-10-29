import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mplc


def demonstrate(loc, names_list, cmap_list, background="white"):
    N = 15000
    x = np.random.rand(N)
    y = np.random.rand(N)
    side_length = 1.181102

    for i in names_list:
        j = names_list.index(i)
        fig = plt.figure(figsize=(side_length*1.7778,side_length))
        ax = fig.add_subplot(111)
        fig.patch.set_facecolor(background)
        ax.patch.set_facecolor(background)

        ax.spines.clear()
        ax.set_xticks([])
        ax.set_yticks([])
        ax.scatter(y, x, c=y, s=10, cmap=cmap_list[j])
        fig.subplots_adjust(top=1,
                            bottom=0,
                            left=0,
                            right=1,
                            hspace=0,
                            wspace=0)
        fig.savefig(f"{loc}{i}.png", dpi=600)
        plt.close()

def brightness(rgb,stop=0):
    if (stop < -3 or stop >3):
        print('''Error, stop values must be between -2 and 2.''')
        return
#    print(f'stop:{stop} changes brightness from ',end="")
    hsv = mplc.rgb_to_hsv(rgb)
    v = hsv[2]
#    print(f'{round(v*100,2)}% to ', end="")
    if stop > 0:
        x = (1-v)/4
    else:
        x = v/4
    hsv[2] = v+stop*x
#    print(f'{round(hsv[2]*100,2)}%')
    rgb = mplc.hsv_to_rgb(hsv)
    return(rgb)

def saturation(rgb,stop=0):
    if (stop < -3 or stop >3):
        print('''Error, stop values must be between -2 and 2.''')
        return
#    print(f'stop:{stop} changes brightness from ',end="")
    hsv = mplc.rgb_to_hsv(rgb)
    s = hsv[1]
#    print(f'{round(v*100,2)}% to ', end="")
    if stop > 0:
        x = (1-s)/4
    else:
        x = s/4
    hsv[1] = s+stop*x
#    print(f'{round(hsv[2]*100,2)}%')
    rgb = mplc.hsv_to_rgb(hsv)
    return(rgb)



def convert_to_rgb(rgb):
    for i in rgb:
        print(f'{int(round(i*255,0))}\t', end="")
    print()
    return

if __name__ =="__main__":

    run_test = [0,-2,-1,1,2,]
    test_col = [(0.00392156862745098, 0.10980392156862745, 0.2549019607843137),
                (0.9490196078431372, 0.9098039215686274, 0.7647058823529411),
                (0.9607843137254902, 0.6352941176470588, 0.09803921568627451),
                (0.9490196078431372, 0.4627450980392157, 0.07058823529411765),
                (0.8549019607843137, 0.16470588235294117, 0.01568627450980392)]

    for c in test_col:
        for i in run_test:
    #        print(i)
            convert_to_rgb(brightness(c,i))
            for i in run_test:
                convert_to_rgb(saturation(c,i))


#    to_cmap = mplc.LinearSegmentedColormap.from_list
#    c_map =  to_cmap("test", ["#011c41","#F2E8C3","#F5A219","#F27612","#DA2A04"])
#    n = 5
#    c_map = c_map._resample(n)
#
#
#    output=[]
#
#    for i in range(c_map.N):
#        rgb = c_map(i)[:3] # will return rgba, we take only first 3 so we get rgb
#        print(rgb)
#        for i in rgb:
#            print(f'{int(round(i*255,0))}\t', end="")
#        print()
#
