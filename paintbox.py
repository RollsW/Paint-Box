import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mplc
from pylab import cm

plt.close("all")

def get_hex(name,n=5):
    '''takes a matplotlib colormap and returns a number (n) of sampled
    hex colours from the map.'''
    cmap = cm.get_cmap(name, n)
    output_list =[]
    for i in range(cmap.N):
        rgb = cmap(i)[:3]
        output_list.append(mplc.rgb2hex(rgb))
    return(output_list)

def value_calc(stop, value=0.5):
    '''returns a value between 0 and 1 based on an input value and a "stop"
    value (between 0 and 3) which corresponds to 2 equidistant points between
    value and zero, and 2 equidistant points between 0 and 1
    for example: input value 0.5

    stop    result
    0       0.16
    1       0.33
    2       0.66
    3       0.83
    '''
    possible_stops = [0,1,2,3]
    if not stop in possible_stops:
        return "error"
    if stop == 0:
        x = value/3
        return value-2*x
    if stop == 1:
        x = value/3
        return value-x
    if stop == 2:
        x = (1-value)/3
        return value+x
    if stop == 3:
        x = (1-value)/3
        return value+x*2


def modify(name, colours, modification="b", stop=0):
    '''
    takes an matplotlib colormap and modifies either saturation or brightness
    returns a matplotlib colormap:
        name (map name)
        colours (colormap)
        modification ("b" for brightness or "s" for saturation)
        stop (integer between 0 (low/dark) and 3 (high/light))
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

class PaintBox():
    ''' manages a number of different matplotlib colormaps'''
    def __init__(self, name, colours):
        '''
        Accepts multiple colour formats:
            hex "#xxxxxx"
            decimal RGB: [0.x,0.x,0.x] or (0.x,0.x,0.x)
            integer RGB: [255,255,255] or (255,255,255)
            or a mixture (if you're feeling perverse.)
        converts the colours to a matplotlib colormap and then adds colormaps
        with varying degrees of brightness, and saturation.'''
        self.name = name
        self.savepath = ""
        self.palette_path = ""
        self.colours_list = []
        for c in colours:
            #convert everything into a common format
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
        self.basemap = mplc.LinearSegmentedColormap.from_list(self.name,self.colours_list)
        self.basemap_light2 = modify(self.name+" light+",self.colours_list, modification="b", stop=3)
        self.basemap_light = modify(self.name+" light",self.colours_list, modification="b", stop=2)
        self.basemap_dark = modify(self.name+"dark",self.colours_list, modification="b", stop=1)
        self.basemap_dark2 = modify(self.name+" dark+",self.colours_list, modification="b", stop=0)
        self.basemap_sat2 = modify(self.name+" saturated+",self.colours_list, modification="s", stop=3)
        self.basemap_sat = modify(self.name+" saturated",self.colours_list, modification="s", stop=2)
        self.basemap_dsat = modify(self.name+" desaturated",self.colours_list, modification="s", stop=1)
        self.basemap_dsat2 = modify(self.name+" desaturated+",self.colours_list, modification="s", stop=0)

        self.mapslist = [self.basemap,
                         self.basemap_light,
                         self.basemap_light2,
                         self.basemap_dark,
                         self.basemap_dark2,
                         self.basemap_sat,
                         self.basemap_sat2,
                         self.basemap_dsat,
                         self.basemap_dsat2]

    def swatch_location(self,path):
        '''sets up where we want the swatches sent'''
        self.savepath = path
        if not os.path.exists(self.savepath):
            os.makedirs(self.savepath)

    def swatches(self,background="black", save=False):
        ''' generates an image for each colormap and either saves them to the
        swatch location, or displays them as matplotlib figures'''
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
            ax.scatter(y, x, c=y, s=10, cmap=i, alpha=0.8)
            fig.subplots_adjust(top=1,
                                bottom=0,
                                left=0,
                                right=1,
                                hspace=0,
                                wspace=0)
            if save is True:
                plt.savefig(f"{self.savepath}\\{i.name}.png",
                dpi=50,
                transparent=False)
                plt.close(fig)
        print(f"Swatches saved to {self.savepath}")

    def export(self, path):
        '''exports a .gpl file (Gimp palette, compatible with inkscape)
        to the specified path'''
        file_name = f"{path}\\{self.name}.gpl"
        with open(file_name,"w") as palette_file:
            print(f"GIMP Palette\nName: {self.name}\nColumns: 0\n#\n", file=palette_file)
        print(f"Generating {file_name}")
        l = len(self.colours_list)
        for c_map in self.mapslist:
            x = c_map._resample(l)
            for n in range(l):
                rgb = mplc.to_rgb(x(n))
                with open(file_name,"a") as palette_file:
                    print(f"{int(rgb[0]*255)}\t{int(rgb[1]*255)}\t{int(rgb[2]*255)}\t {c_map.name} (colour {n+1})", file=palette_file)

if __name__ == "__main__":
#   good sources of colourschemes include:

#    Colormind: http://colormind.io/
#    palette = ["#1F1314","#913D33","#C77B53","#D1BF92","#9F9782"]
#    palette = ["#2B344B","#69829D","#798EA6","#ADA68A","#BC8064"]

#    Images - use colorthief to get most common colours
#    from colorthief import ColorThief as ct
#    color_thief = ct(r'C:\Users\wjrol\Desktop\sunset-3320015_1280.jpg')
#    palette = color_thief.get_palette(color_count=6, quality=1)

#   Adobe colour CC https://color.adobe.com/explore/
#    palette = ["#112f41","#068587","#4fb99f","#f2b134","#ed553b"]
#    palette = ["#f3cb60","#f5b74d","#f26d40","#d95242","#a83738"]
#   palette = ["#142c41","#f2ebc3","#f5a219","#f27612","#b5291d"]

#   direct from matplotlib
    palette = get_hex('plasma',5)

    x = PaintBox("test",palette)
    x.palette_path = r".\test" # for inkscape use r"C:\Users\[yourname]\AppData\Roaming\inkscape\palettes"
    x.swatch_location(r".\test")
    x.swatches(save=True)
    x.export(x.palette_path)


