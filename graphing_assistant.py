import matplotlib.pyplot as plt
import numpy as np
import math

class Graphing_Assistant: 

    def __init__(self): 
        pass
    
    from analysis import analyze_histogram

    def get_quarter(self,date):
        month = int(date.split('-')[1])  # Extracting the month from the date string
        quarter = math.ceil(month / 3)  # Calculating the quarter based on the month
        return quarter

    def plot_histogram(self,data,title,flags,lines): 
        return
        # return
        # # num_bins = int(1 + np.log2(len(data))) #sturges
        # # print("number of bins:", num_bins)
        # # num_bins = int((max(data) - min(data)) / bin_width) #scott
        # # num_bins = int(np.sqrt(len(data))) #square root
        # num_bins = 100 
        # # num_bins = int(np.max(data)-np.min(data))
        # len_data, len_title, len_flags, len_lines= len(data),len(title),len(flags), len(lines)

        # if not(len_data == len_title and len_data == len_flags and len_data == len_lines):
        #     print("===Graphing-Assistant=====: Not all provided arrays have the same length! Killing the process.")
        #     exit(1)
        
        # colors_list = ['cyan','black','brown','green','gray','pink','cyan', 'purple','yellow','blue','orange','magenta']
        # color_idx =0

        # for idx in range(len_data):
        #     mean_value = np.mean(data[idx])
        #     median_value = np.median(data[idx])      
        #     hist_values, bin_edges, _=plt.hist(data[idx], bins=num_bins, edgecolor='k')  # Adjust the number of bins as needed
        #     mean_frequency = np.mean(hist_values)
        #     median_frequency = np.median(hist_values)

        #     if "x" in lines[idx].keys():
        #         plt.axvline(lines[idx]["x"], color=colors_list[color_idx], linestyle='solid', linewidth=2, label=f'asked x1: {title[idx]["x"]:.2f}')
        #     if "y" in lines[idx].keys():
        #         plt.axhline(title[idx]["y"], color=colors_list[color_idx+1], linestyle='solid', linewidth=2, label=f'Median y: {title[idx]["y"]:.2f}')
            

        #     plt.axvline(mean_value, color=colors_list[color_idx+2], linestyle='dashed', linewidth=2, label=f'Mean x1: {mean_value:.2f}')
        #     plt.axvline(median_value, color=colors_list[color_idx+3], linestyle='dashed', linewidth=2, label=f'Median x1: {median_value:.2f}')
        #     plt.axhline(mean_frequency, color=colors_list[color_idx+4], linestyle='dashed', linewidth=4, label=f'Mean y: {mean_frequency:.2f}')
        #     plt.axhline(median_frequency, color=colors_list[color_idx+5], linestyle='dashed', linewidth=4, label=f'Median y: {median_frequency:.2f}')
        #     plt.legend()
        #     plt.xlabel(f"{title[idx]}")
        #     plt.ylabel('Frequency')
        #     plt.title(f"Histogram of {title[idx]}")
        #     plt.grid(True)
        #     color_idx +=6


        # if any(flags):
        #     plt.show()

    def plot_xy_single(self,datax,datay,title,xlabel,ylabel): 

        mean_value = np.mean(datay)
        median_value = np.median(datay)
        plt.scatter(datax, datay, marker='o', linestyle='-')
        # add mean and median lines
        plt.axhline(mean_value, color='purple', linestyle='dashed', linewidth=1, label=f'Mean y: {mean_value:.2f}')
        plt.axhline(median_value, color='brown', linestyle='dashed', linewidth=1, label=f'Median y: {median_value:.2f}')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)

        plt.show()

    def plot_xy_same(self,datax,datay,title,xlabel,ylabel): 

        len_datax, len_datay, len_title, len_xlabel, len_ylabel= len(datax),len(datay),len(title),len(xlabel), len(ylabel)

        if not(len_datax == len_datay and len_datax == len_title and len_datax == len_xlabel and len_datax == len_ylabel):
            print("===Graphing-Assistant=====: Not all provided arrays have the same length! Killing the process.")
            exit(1)
        
        
        for idx in range (len_datax):
            if len(datay[idx]) == 0:
                continue
            mean_value = np.mean(datay[idx])
            median_value = np.median(datay[idx])
            plt.plot(datax[idx], datay[idx], marker='o', linestyle='-')
            # add mean and median lines
            plt.axhline(mean_value, color='purple', linestyle='dashed', linewidth=4, label=f'Mean y: {mean_value:.2f}')
            plt.axhline(median_value, color='brown', linestyle='dashed', linewidth=4, label=f'Median y: {median_value:.2f}')
            plt.xlabel(xlabel[idx])
            plt.ylabel(ylabel[idx])
            plt.title(title[idx])
        
        plt.show()

    def plot_xy_seperate(self,datax,datay,title,xlabel,ylabel): 

        len_datax, len_datay, len_title, len_xlabel, len_ylabel= len(datax),len(datay),len(title),len(xlabel), len(ylabel)
        if not(len_datax == len_datay and len_datax == len_title and len_datax == len_xlabel and len_datax == len_ylabel):
            print("===Graphing-Assistant=====: Not all provided arrays have the same length! Killing the process.")
            exit(1)
            
        fig, ax = plt.subplots(len_datax, 1, sharex=False) 
        for idx in range (len_datax):
            if len(datay[idx]) == 0:
                continue

            max_index = np.argmax(datay[idx])
            max_x = datax[idx][max_index]
            max_y = datay[idx][max_index]
            mean_value = np.mean(datay[idx])
            median_value = np.median(datay[idx])
            # ax[idx].plot(datax[idx], datay[idx], marker='o', linestyle='-')
            for i in range(len(datax[idx]) - 1):
                quarter= self.get_quarter(datax[idx][i])

                if quarter == 1:
                    ax[idx].plot([datax[idx][i], datax[idx][i + 1]], [datay[idx][i], datay[idx][i + 1]], color='blue')  
                elif quarter == 2:
                    ax[idx].plot([datax[idx][i], datax[idx][i + 1]], [datay[idx][i], datay[idx][i + 1]], color='red') 
                elif quarter == 3:
                    ax[idx].plot([datax[idx][i], datax[idx][i + 1]], [datay[idx][i], datay[idx][i + 1]], color='green') 
                elif quarter == 4:
                    ax[idx].plot([datax[idx][i], datax[idx][i + 1]], [datay[idx][i], datay[idx][i + 1]], color='brown')               

            # add mean and median lines
            ax[idx].axhline(mean_value, color='purple', linestyle='dashed', linewidth=1, label=f'Mean y: {mean_value:.2f}')
            ax[idx].axhline(median_value, color='brown', linestyle='dashed', linewidth=1, label=f'Median y: {median_value:.2f}')
            ax[idx].set_xlabel(xlabel[idx])
            ax[idx].set_ylabel(ylabel[idx])
            ax[idx].set_title(title[idx])
            # ax[idx].legend()
            ax[idx].tick_params(axis='x', labelrotation=90,labelsize=6)

            ax[idx].scatter(max_x, max_y, color='red', label=f"Highest point: ({max_x}, {max_y:.2f})")
            ax[idx].annotate(f"({max_x}, {max_y:.2f})", (max_x, max_y), textcoords="offset points", xytext=(-5, -10), ha='center')
            ax[idx].grid(which='both', linestyle='-', linewidth='0.5', color='black')

        plt.subplots_adjust(hspace=0.5, bottom=0.1)
        plt.show()

