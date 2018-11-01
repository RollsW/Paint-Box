import matplotlib.colors as mplc
import colormap_to_png as c2i

def make_colormap(seq):
    """Return a LinearSegmentedColormap
    seq: a sequence of floats and RGB-tuples. The floats should be increasing
    and in the interval (0,1).
    """
    seq = [(None,) * 3, 0.0] + list(seq) + [1.0, (None,) * 3]
    cdict = {'red': [], 'green': [], 'blue': []}
    for i, item in enumerate(seq):
        if isinstance(item, float):
            r1, g1, b1 = seq[i - 1]
            r2, g2, b2 = seq[i + 1]
            cdict['red'].append([item, r1, r2])
            cdict['green'].append([item, g1, g2])
            cdict['blue'].append([item, b1, b2])
    return mplc.LinearSegmentedColormap('CustomMap', cdict)

c = mplc.ColorConverter().to_rgb
rvb = make_colormap(
    [c("#011c41"), c('#F2E8C3'), 0.25,
     c('#F2E8C3'), c('#F5A219'),0.5,
     c('#F5A219'),c('#F27612'),0.75,
     c('#F27612'),c('#DA2A04')])


c_map =  mplc.LinearSegmentedColormap.from_list("test", ["#011c41","#F2E8C3","#F5A219","#F27612","#DA2A04"])

c2i.demonstrate(r"",["test1", "test2"],[rvb,c_map])