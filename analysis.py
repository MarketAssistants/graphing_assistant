import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import skew, kurtosis,mode


def analyze_histogram(self,data,plot=False):

    if plot:
        plt.hist(data, bins=20, color='blue', alpha=0.7)
        plt.title('Histogram')
        plt.xlabel('X-axis label')
        plt.ylabel('Frequency')
        plt.show()

    # Step 5: Analyze the Histogram

    # Central Tendency
    mean_value = np.mean(data)
    median_value = np.median(data)
    mode_value = float(mode(data).mode)  # Using mode from scipy.stats

    # Spread
    range_value = np.ptp(data)
    std_dev = np.std(data)

    # Skewness
    skewness = skew(data)

    # Modality
    kurt = kurtosis(data)
    if kurt > 3:
        modality = 'Leptokurtic Tails are fatter (more outliers at tails), peak is higher'  # Tails are fatter, peak is higher
    elif kurt < 3:
        modality = 'Platykurtic = Tails are thinner (less outliers at tails), peak is lower'  # Tails are thinner, peak is lower
    else:
        modality = 'Mesokurtic = Similar to normal distribution'   # Similar to normal distribution

    # Outliers
    lower_bound = mean_value - 2 * std_dev
    upper_bound = mean_value + 2 * std_dev
    outliers = [x for x in data if x < lower_bound or x > upper_bound]



    results_dict = {
    "Mean": mean_value,"Median": median_value, "Mode":mode_value, 
    "Spread (Standard Deviation)":std_dev, "Skewness": skewness, 
    "Modality": modality, "Outliers": outliers }
    
    return results_dict

#locally tested
# results = analyze_histogram(None, np.random.randn(1000))