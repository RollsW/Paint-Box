import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mplc
from pylab import cm

def get_hex(name,n=5):
    cmap = cm.get_cmap(name, n)
    output_list =[]
    for i in range(cmap.N):
        rgb = cmap(i)[:3] # will return rgba, we take only first 3 so we get rgb
        output_list.append(mplc.rgb2hex(rgb))
    return(output_list)


def value_calc(stop, value=0.5):
    ''' stops = 0,1,2,3'''
    possible_stops = [0,1,2,3]
    if not stop in possible_stops:
        return "error"
    if stop == 0:
        x = value/3
        return value-x
    if stop == 1:
        x = value/3
        return value-2*x
    if stop == 2:
        x = (1-value)/3
        return value+x
    if stop == 3:
        x = (1-value)/3
        return value+x*2


def modify(name, colours, modification="b", stop=0):
    '''
    modifications = brightness [0 - 3]
                    saturation [0 - 3]
    stop = intesntity

    '''
    key = 0
    
    hsv_colours = []
    output = []
    hsv_output = ()
    for col in colours:
        rgb_col = mplc.to_rgb(col)
        hsv_col = mplc.rgb_to_hsv(rgb_col)
        hsv_colours.append(hsv_col)
    if modification is "b":
        key = 2
    if modification is "s":
        key = 1
    for hsv_col in hsv_colours:
        hsv_output = [hsv_col[0],hsv_col[1],hsv_col[2]]
        hsv_output[key] = value_calc(stop,hsv_output[key])
        hsv_output = tuple(hsv_output)
        rgb_output = mplc.hsv_to_rgb(hsv_output)
        output.append(rgb_output)
    output = mplc.LinearSegmentedColormap.from_list(name,output)
    return output

def swatch(mpl_map,background="black"):
    N = 15000
    x = np.random.rand(N)
    y = np.random.rand(N)
    side_length = 1.181102
    fig = plt.figure(figsize=(side_length*1.7778,side_length))
    ax = fig.add_subplot(1,1,1)
    fig.patch.set_facecolor(background)
    ax.patch.set_facecolor(background)
    ax.spines.clear()
    ax.set_xticks([])
    ax.set_yticks([])
    ax.scatter(y, x, c=y, s=10, cmap=mpl_map)
    fig.subplots_adjust(top=1,
                        bottom=0,
                        left=0,
                        right=1,
                        hspace=0,
                        wspace=0)


class PaintBox():
    '''
    Accepts multiple colour formats:
        hex "#xxxxxx"
        decimal RGB: [0.x,0.x,0.x] or (0.x,0.x,0.x)
        integer RGB: [255,255,255] or (255,255,255)
        or a mixture (if you're feeling perverse.)
    '''
    def __init__(self, name, colours):
        # convert everything into a common format.
        self.dummy_list = mplc.LinearSegmentedColormap.from_list(name="blank_colours",colors=[[1,1,1],[0.5,0.5,0.5],[0.0,0.0,0.0]])
        self.name = name
        self.colours_list = []
        self.basemap = self.dummy_list
        self.savepath = ""
        self.basemap_light = self.dummy_list
        self.basemap_light2 = self.dummy_list
        self.basemap_dark = self.dummy_list
        self.basemap_dark2 = self.dummy_list
        self.basemap_sat = self.dummy_list
        self.basemap_sat2 = self.dummy_list
        self.basemap_dsat = self.dummy_list
        self.basemap_dsat2 = self.dummy_list
        self.mapslist = [self.basemap,
                         self.basemap_light,
                         self.basemap_light2,
                         self.basemap_dark,
                         self.basemap_dark2,
                         self.basemap_sat,
                         self.basemap_sat2,
                         self.basemap_dsat,
                         self.basemap_dsat2]

        for c in colours:
            if c[0] is "#" and len(c) is 7:
                x = mplc.hex2color(c)
                self.colours_list.append(x)
            elif (isinstance(c, (tuple, list))) and (len(c) is 3) and (isinstance(c[0], int)):
                c2 = []
                for i in c:
                    c2.append(i/255)
                self.colours_list.append(tuple(c2))
            elif (isinstance(c, (tuple, list))) and (len(c) is 3) and (isinstance(c[0], float)):
                c2 = []
                for i in c:
                    c2.append(i)
                self.colours_list.append(tuple(c2))
        self.basemap = mplc.LinearSegmentedColormap.from_list(self.name+"_base",self.colours_list)
        self.basemap_light = modify(self.name+"_light2",self.colours_list, modification="b", stop=3)
        self.basemap_light2 = modify(self.name+"_light",self.colours_list, modification="b", stop=2)
        self.basemap_dark = modify(self.name+"_dark2",self.colours_list, modification="b", stop=1)
        self.basemap_dark2 = modify(self.name+"_dark",self.colours_list, modification="b", stop=0)
        self.basemap_sat = modify(self.name+"_sat2",self.colours_list, modification="s", stop=3)
        self.basemap_sat2 = modify(self.name+"_sat",self.colours_list, modification="s", stop=2)
        self.basemap_dsat = modify(self.name+"_dsat2",self.colours_list, modification="s", stop=1)
        self.basemap_dsat2 = modify(self.name+"_dsat",self.colours_list, modification="s", stop=0)
        
        self.mapslist = [self.basemap,
                         self.basemap_light,
                         self.basemap_light2,
                         self.basemap_dark,
                         self.basemap_dark2,
                         self.basemap_sat,
                         self.basemap_sat2,
                         self.basemap_dsat,
                         self.basemap_dsat2]

    def save_location(self,path):
        self.savepath = path
        if not os.path.exists(self.savepath):
            os.makedirs(self.savepath)

    def swatches(self,background="black", save=False):
        N = 15000
        x = np.random.rand(N)
        y = np.random.rand(N)
        side_length = 1.181102

        for i in self.mapslist:
            x = np.random.rand(N)
            y = np.random.rand(N)
            fig = plt.figure(figsize=(side_length*1.7778,side_length))
            ax = fig.add_subplot(1,1,1)
            fig.patch.set_facecolor(background)
            ax.patch.set_facecolor(background)
            ax.spines.clear()
            ax.set_xticks([])
            ax.set_yticks([])
            ax.scatter(y, x, c=y, s=10, cmap=i)
            fig.subplots_adjust(top=1,
                                bottom=0,
                                left=0,
                                right=1,
                                hspace=0,
                                wspace=0)
            if save is True:
                plt.savefig(f"{self.savepath}\\{i.name}.png",
                dpi=300,
                transparent=False)
            plt.close(fig)



if __name__ == "__main__":

    y = ["#2b3a42","#3f5866","#bdd3de","#f0f0df","#ff8f00"]


#    y = get_hex('magma',6)
    x = PaintBox("test",y)
    x.save_location(r".\\test")
    x.swatches(save=True)
