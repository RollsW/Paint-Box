'''generates colour gradients from matplotlib cmaps
'''
from pylab import cm
import matplotlib.colors as mplc
import pandas as pd

def gradient(n, cmap='cividis', col_format="rgb"):
    '''returns [n] gradient points in rgb format as a list of tuples'''
    cmap = cm.get_cmap(cmap, n)
    output = []
    for i in range(cmap.N):
        rgb = cmap(i)[:3] # will return rgba, we take only first 3 so we get rgb
        out = mplc.rgb2hex(rgb)
        if col_format == "rgb":
            out = mplc.hex2color(out)
            out_temp = []
            for o in out:
                out_temp.append(int(255*o))
            output.append(tuple(out_temp))
        else:
            output.append(out)
    return output

def scheme(cols):
    df = pd.DataFrame()
    df["cols"] = cols
    base_shade = []
    for col in cols:
        lowest = min(col)
        new_col = []
        for c in col:
            c = c-lowest
            new_col.append(c)
        col = tuple(new_col)
        base_shade.append(col)
    df["base_shade"]=base_shade
    return df

#        i2 = []
#        i3
#        i4
#        i5
#


#        hsv = mplc.rgb_to_hsv(i)
#        hsv[1] = hsv[1]/desat
#        rgb =  mplc.hsv_to_rgb(hsv)
#        rgb = [int(i) for i in rgb]
#        output.append(tuple(rgb))
#
#







if __name__ == "__main__":
    x = gradient(10, col_format="rgb")
    y = scheme(x)
    print(y)