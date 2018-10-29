import numpy as np
import matplotlib.pyplot as plt


# Fixing random state for reproducibility
#np.random.seed(19680801)

# Compute areas and colors
def demonstrate(loc, names_list, cmap_list):
    N = 15000
    background='black'
    x = np.random.rand(N)
    y = np.random.rand(N)
    side_length = 1.181102

    for i in names_list:
        j = names_list.index(i)
        fig = plt.figure(figsize=(side_length*1.7778,side_length))
        ax = fig.add_subplot(111)
        fig.patch.set_facecolor(background)
        ax.patch.set_facecolor(background)
        ax.scatter(y, x, c=y, s=10, cmap=cmap_list[j])
        ax.spines.clear()
        ax.set_xticks([])
        ax.set_yticks([])
        fig.subplots_adjust(top=1,
                            bottom=0,
                            left=0,
                            right=1,
                            hspace=0,
                            wspace=0)
        fig.savefig(f"{loc}{i}.png", dpi=200)

if __name__ =="__main__":
    names_list = ["4","5","6"]
    cmap_list = ["viridis","magma","plasma"]
    demonstrate("",names_list,cmap_list)
