import matplotlib.pyplot as plt
import numpy as np

class Graphing_Assistant: 

    def __init__(self): 
        pass

    def plot_histogram(self,data1,data2,title1,title2,flags): 
        # num_bins = int(1 + np.log2(len(data))) #sturges
        # print("number of bins:", num_bins)
        # num_bins = int((max(data) - min(data)) / bin_width) #scott
        # num_bins = int(np.sqrt(len(data))) #square root
        num_bins = 100 
        # num_bins = int(np.max(data)-np.min(data))

        # Create a histogram
        if flags[0]:
            plt.hist(data1, bins=num_bins, edgecolor='k')  # Adjust the number of bins as needed
            plt.xlabel(f"{title1}")
            plt.ylabel('Frequency')
            plt.title(f"Histogram of {title1}")
            plt.grid(True)

        if flags[1]: 
            plt.hist(data2, color = "red", bins=num_bins, edgecolor='k')  # Adjust the number of bins as needed
            plt.xlabel(f"{title1}")
            plt.ylabel('Frequency')
            plt.title(f"Histogram of {title1}")
            plt.grid(True)
           
        if flags[0] or flags[1]:
            plt.show()



    def plot_xy(self,datax,datay,title,xlabel,ylabel): 
        plt.plot(datax, datay, marker='o', linestyle='-')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()

