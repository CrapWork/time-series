import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

def wrangle_data():
    return pd.read_excel('/Users/garrettwilliford/Downloads/fitbit/fitbit_data.xlsx')


#data = wrangle_data()



def active_data(data):
    sns.lineplot('Date','Minutes Sedentary', data = data)
    sns.lineplot('Date','Minutes Fairly Active', data = data)
    sns.lineplot('Date', 'Minutes Very Active', data = data)
    sns.lineplot('Date', 'Minutes Lightly Active', data = data)
    plt.show()


#subset = data.groupby('Date')['Minutes Sedentary'].mean().reset_index()


#subset = subset.set_index('Date')


#subset = pd.DataFrame(subset['Minutes Sedentary'].resample('W').mean())




def time_predict(data, predict, start_date = '2018-10-27',predict_date ='2018-10-27',info_plots = False, stats_info = False):
    y = data.groupby('Date')[predict].mean()
    mod = sm.tsa.statespace.SARIMAX(y,
                            order=(1, 1, 1),
                            seasonal_order=(1, 1, 0, 12),
                            enforce_stationarity=False,
                            enforce_invertibility=False)
    results = mod.fit()
    decomposition = sm.tsa.seasonal_decompose(y, model='additive')
    if info_plots:
        results.plot_diagnostics(figsize=(16, 8))
        plt.show()
        fig = decomposition.plot()
        plt.show()
    pred = results.get_prediction(start=pd.to_datetime(start_date), dynamic=False)
    pred_ci = pred.conf_int()
    print(pred)
    ax = y['2018-4':].plot(label='observed')
    pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
    ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)
    plt.legend()
    plt.show()
    if stats_info:
        y_forecasted = pred.predicted_mean
        y_truth = y['2018-10-27':]
        mse = ((y_forecasted - y_truth) ** 2).mean()
        print('<<<<<>>>>><|_STATS_INFO_|><<<<<>>>>>')
        print('MSE:  ' + str(mse))
        print('RMSE: ' + str(round(np.sqrt(mse), 2)))



#print(data['Calories Burned'].max())


#print(data)
#time_predict(data,'Calories Burned', infostats_info = True)
