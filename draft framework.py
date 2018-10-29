import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mplc

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
        j = 0
        for i in self.mapslist:
            j = j+1
            fig = plt.figure(j, figsize=(side_length*1.7778,side_length))
            ax = fig.add_subplot(111)
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
                plt.savefig(f"{self.savepath}\\{i.name} {j}.png",
                dpi=300,
                transparent=False)



if __name__ == "__main__":
    test = ["#ffffff", (1.0, 1.0, 1.0), [1.0, 1.0, 1.0], (255, 255, 255), [255, 255, 255]]
    x = PaintBox("test",test)
    print(x.colours_list)

    test = ["#011c41","#F2E8C3","#F5A219","#F27612","#DA2A04"]
    x = PaintBox("_another_test",test)
    print(x.colours_list)
    x.save_location(r".\\test")
    x.swatches(save=True)
