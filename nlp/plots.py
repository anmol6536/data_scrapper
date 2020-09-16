import matplotlib.pyplot as plt
import numpy as np

def overview(df, fig):
    cols = [*df]
    rows = len(cols)/3
    height = round(rows*20)
    count = 1
    for i in cols:
        to_plot = df[i].value_counts()
        cmap = plt.cm.Pastel2
        colors = cmap(np.linspace(0., 1., len(to_plot)))

        if (to_plot.shape[0]<20) & (to_plot.shape[0]>1):
            ax = fig.add_subplot(rows+1, 3, count)
            ax.pie(to_plot, labels = [*to_plot.index], colors = colors)
            count += 1
            plt.title(i)
            plt.legend()
    return
