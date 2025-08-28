# import matplotlib.pyplot as plt
# import numpy as np

from graphing_assistant import Graphing_Assistant
# # Generate example data
# data = np.random.randn(1000)

# # Create a histogram
# plt.hist(data, bins=20, color='blue', alpha=0.7, edgecolor='black', label='Data')

# # Add analysis information using plt.text()
# plt.text(1.5, 50, 'Mean: {:.2f}'.format(np.mean(data)), fontsize=12, color='red')
# plt.text(1.5, 45, 'Median: {:.2f}'.format(np.median(data)), fontsize=12, color='green')
# plt.text(1.5, 40, 'Std Dev: {:.2f}'.format(np.std(data)), fontsize=12, color='purple')

# # Add labels and legend
# plt.title('Histogram with Analysis Information')
# plt.xlabel('X-axis label')
# plt.ylabel('Frequency')
# plt.legend()

# # Show the plot
# plt.show()

def formula(a,b): 
    datax= [] 
    datay = []

    val_1 = 100
    val_2 = 300
    max_prc = (val_2-val_1)/val_1*100



    for prc_step_b in range(101): 
        prc_step = max_prc*prc_step_b/100
        cur = val_1*(1+prc_step/100)
        datax.append(prc_step_b)
        datay.append(max_prc-(((cur-val_1)/val_1)*100+((val_2-cur)/cur)*100))

    return datax, datay



graphing_guy = Graphing_Assistant()

data_x= [] 
data_y = []


x,y = formula(100,200) 
data_x.append(x) 
data_y.append(y)

x,y = formula(100,300) 
data_x.append(x) 
data_y.append(y)

graphing_guy.plot_xy_same(data_x,data_y,["test func","test_func"],['100-200','100-300'],['100-200','100-300'])