from numpy.core.numeric import roll
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt

def adf_test(dataframe) -> None:
    adf, pvalue, _, _, critical_values, _ = adfuller(dataframe)
    stationary_value = pvalue <= 0.05
    test_critical_value = round(critical_values['5%'], 2)
    
    print(
        f"Is the time series stationary ? {stationary_value}\n"
        f"Test statistic value (adf) =  {round(adf,2)}\n" 
        f"P value = {round(pvalue,2)}\n" 
        f"test critical value ('5%') = {test_critical_value}")


def plot_mean_Std(dataframe, window):
    rolling_mean = dataframe.rolling(window = window).mean()
    # print(rolling_mean)
    rolling_std = dataframe.rolling(window=window).std()
    # print(rolling_std)
    plt.plot(dataframe, label = "series")
    plt.plot(rolling_mean, label = "rolling mean")
    plt.plot(rolling_std, label = "rolling std")
    plt.legend(loc = "best")
    plt.show()


def stationary(dataframe, window=12):
    plot_mean_Std(dataframe, window)
    adf_test(dataframe) 
