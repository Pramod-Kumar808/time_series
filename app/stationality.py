from statsmodels.tsa.stattools import adfuller


def adf_test(dataframe) -> None:
    adf, pvalue, _, _, critical_values, _ = adfuller(dataframe)
    stationary_value = pvalue <= 0.05
    test_critical_value = round(critical_values['5%'], 2)
    print(
        f"Is the time series stationary ? {stationary_value}\n"
        f"Test statistic value (adf) =  {round(adf,2)}\n" 
        f"P value = {round(pvalue,2)}\n" 
        f"test critical value ('5%') = {test_critical_value}")