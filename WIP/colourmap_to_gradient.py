'''generates colour gradients from matplotlib cmaps
'''
from pylab import cm
import palettable
import matplotlib.colors as mplc
import webbrowser
import matplotlib.pyplot as plt
import numpy as np

head = """<!DOCTYPE html>
<html><head><style>
p {text-align: left;
    padding-bottom: 20px;
    padding-left: 20%;
    padding-right: 20px;
    padding-top: 20px;
   font-size: 30px;
   margin:-0px}
</style></head><body>"""

foot="""</body></html>"""

c = {'red':[(0,0.00392156862745098,0.00392156862745098),
            (0.25,0.9490196078431372,0.9490196078431372),
            (0.5,0.9607843137254902,0.9607843137254902),
            (0.75,0.9490196078431372,0.9490196078431372),
            (1,0.8549019607843137,0.8549019607843137)],
     'green':[(0,0.10980392156862745,0.10980392156862745),
             (.25,0.9098039215686274,0.9098039215686274),
             (.5,0.6352941176470588,0.6352941176470588),
             (.75,0.4627450980392157,0.4627450980392157),
             (1,0.16470588235294117,0.16470588235294117)],
     'blue':[(0,0.2549019607843137,0.2549019607843137),
             (0.25,0.7647058823529411,0.7647058823529411),
             (0.5,0.09803921568627451,0.09803921568627451),
             (0.75,0.07058823529411765,0.07058823529411765),
             (1,0.01568627450980392,0.01568627450980392)],
     'alpha':[(0.0, 1, 1),
             (0.25, 1, 1),
             (0.5, 1, 1),
             (0.75, 1, 1),
             (1.0, 1, 1)],
     '_gamma':1.0}

def gradient(n, cmap='cividis'):
    '''returns [n] gradient points in rgb format as a list of tuples'''

    cmap = cmap._resample(n)
    output = []
    for i in range(cmap.N):
        rgb = cmap(i)[:3] # will return rgba, we take only first 3 so we get rgb
        out = mplc.rgb2hex(rgb)
        output.append(out)
    return output

def fs(filename, content,switch="a"):
    with open(filename, switch) as myfile:
        myfile.write(content)

def black_white(hex):
    '''requires a hex string
    decides whether black or white text will show up better'''
    rgb = mplc.hex2color(hex)
    dec = rgb[0]*255+rgb[1]*255+rgb[2]*255
    if dec < 380:
        out = '#ffffff'
    else:
        out = '#000'
    return(out)

def display(grad,visual=0, name="output"):

    filename = f'{name}.html'
    fs(filename, content=head,switch='w')

    for i in grad:
        textcol = black_white(i)
        html_frag1 ='<div id="container" title="'
        html_frag2 = '" style="background-color:'
        html_frag3 = '"><p style="color:'


        i_rgb = list(mplc.hex2color(i))
        i_rgb[0] = int(i_rgb[0]*255)
        i_rgb[1] = int(i_rgb[1]*255)
        i_rgb[2] = int(i_rgb[2]*255)
        i_rgb = f"&nbsp;&nbsp;({i_rgb[0]},  {i_rgb[1]},  {i_rgb[2]})"
        text = i+i_rgb

        div = html_frag1+i+i_rgb+html_frag2+i+html_frag3+textcol+'">'
        p_end = r'</p></div>'
        fs(filename, div+text+p_end)


    fs(filename, content=foot)
    if visual == 1:
        webbrowser.open_new_tab(filename)
    return

if __name__ == "__main__":
    colmap = palettable.cmocean.sequential.Matter_3
    #full reference for color maps is here https://jiffyclub.github.io/palettable/
    #and here https://matplotlib.org/examples/color/colormaps_reference.html
    colmap=colmap.mpl_colormap
    colmap._segmentdata=c
    colmap = cm.get_cmap("copper")
    x = gradient(7, cmap=colmap)
    display(x,1,'Solar')

#    N = 100
#    array_dg = np.random.uniform(0, 10, size=(N, 2))
#    colors = np.random.uniform(-2, 2, size=(N,))
#    plt.scatter(array_dg[:, 0], array_dg[:, 1], c=colors, cmap=colmap)
#    plt.colorbar()
#    plt.show()
