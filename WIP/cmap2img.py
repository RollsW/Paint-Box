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

if __name__ =="__main__":

#    col_list =['Accent','Accent_r','Blues','Blues_r','BrBG','BrBG_r','BuGn','BuGn_r',
#             'BuPu','BuPu_r','CMRmap','CMRmap_r','Dark2','Dark2_r','GnBu','GnBu_r',
#             'Greens','Greens_r','Greys','Greys_r','OrRd','OrRd_r','Oranges',
#             'Oranges_r','PRGn','PRGn_r','Paired','Paired_r','Pastel1','Pastel1_r',
#             'Pastel2','Pastel2_r','PiYG','PiYG_r','PuBu','PuBuGn','PuBuGn_r','PuBu_r',
#             'PuOr','PuOr_r','PuRd','PuRd_r','Purples','Purples_r','RdBu','RdBu_r',
#             'RdGy','RdGy_r','RdPu','RdPu_r','RdYlBu','RdYlBu_r','RdYlGn','RdYlGn_r',
#             'Reds','Reds_r','Set1','Set1_r','Set2','Set2_r','Set3','Set3_r','Spectral',
#             'Spectral_r','Wistia','Wistia_r','YlGn','YlGnBu','YlGnBu_r','YlGn_r',
#             'YlOrBr','YlOrBr_r','YlOrRd','YlOrRd_r','afmhot','afmhot_r','autumn',
#             'autumn_r','binary','binary_r','bone','bone_r','brg','brg_r','bwr',
#             'bwr_r','cividis','cividis_r','cool','cool_r','coolwarm','coolwarm_r',
#             'copper','copper_r','cubehelix','cubehelix_r','flag','flag_r','gist_earth',
#             'gist_earth_r','gist_gray','gist_gray_r','gist_heat','gist_heat_r',
#             'gist_ncar','gist_ncar_r','gist_rainbow','gist_rainbow_r',
#             'gist_stern','gist_stern_r','gist_yarg','gist_yarg_r','gnuplot',
#             'gnuplot2','gnuplot2_r','gnuplot_r','gray','gray_r','hot','hot_r','hsv',
#             'hsv_r','inferno','inferno_r','jet','jet_r','magma','magma_r',
#             'nipy_spectral','nipy_spectral_r','ocean','ocean_r','pink','pink_r',
#             'plasma','plasma_r','prism','prism_r','rainbow','rainbow_r','seismic',
#             'seismic_r','spring','spring_r','summer','summer_r','tab10','tab10_r',
#             'tab20','tab20_r','tab20b','tab20b_r','tab20c','tab20c_r','terrain',
#             'terrain_r','twilight','twilight_r','twilight_shifted','twilight_shifted_r',
#             'viridis','viridis_r','winter','winter_r']
    col_list =['viridis','magma']



    to_cmap = mplc.LinearSegmentedColormap.from_list
    c_map =  to_cmap("test", ["#011c41","#F2E8C3","#F5A219","#F27612","#DA2A04"])
    n = 5
    c_map = c_map._resample(n)
    print(c_map)
    col_list.append(c_map)

    output=[]

    for i in range(c_map.N):
        rgb = c_map(i)[:3] # will return rgba, we take only first 3 so we get rgb
        for i in rgb:
            print(f'{int(round(i*255,0))}\t', end="")
        print()
#        out = mplc.rgb2hex(rgb)
#        output.append(rgb)
#    print(output)

#    for i in range(len(c_map.N)):
#        r = c_map._segmentdata['red'][i][1]
#        g = c_map._segmentdata['green'][i][1]
#        b = c_map._segmentdata['blue'][i][1]
#        r = int(round(r*255,0))
#        g = int(round(g*255,0))
#        b = int(round(b*255,0))
#        print(f'{r}\t{g}\t{b}')




#    for i in range(len(c_map._segmentdata['red'])):
#        r = c_map._segmentdata['red'][i][1]
#        g = c_map._segmentdata['green'][i][1]
#        b = c_map._segmentdata['blue'][i][1]
#        r = int(round(r*255,0))
#        g = int(round(g*255,0))
#        b = int(round(b*255,0))
#        print(f'{r}\t{g}\t{b}')



    path = r""
    #demonstrate(path,['test','test2','test3'],col_list, background="black")
