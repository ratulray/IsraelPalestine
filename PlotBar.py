import numpy as np
import pickle
import matplotlib.pyplot as plt

def plot_bar(xlabels, Y):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    ## the data
    N = len(Y)
    ## necessary variables
    ind = np.arange(N)                # the x locations for the groups
    width = 0.35                      # the width of the bars
    
    ## the bars
    rects1 = ax.bar(ind, Y, width,
                    color='red')
    
    ax.set_xlim(-width,len(ind)+width)
    ax.set_ylim(0, max(Y)*1.2)
    ax.set_ylabel('Counts')
    ax.set_title('Counts by country')
    #xTickMarks = ['Group'+str(i) for i in range(1,6)]
    ax.set_xticks(ind+width)
    xtickNames = ax.set_xticklabels(xlabels)
    plt.setp(xtickNames, rotation=40, fontsize=10, ha='right')
    
    ## add a legend
    #ax.legend( (rects1[0], rects2[0]), ('Men', 'Women') )
    plt.tight_layout()
    plt.show()
    
if __name__ == "__main__":
    pal = pickle.load(open('palestine.pkl'))
    plot_bar(pal.keys(), pal.values())
