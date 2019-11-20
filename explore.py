import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

def wrangle_data():
    return pd.read_excel('/Users/garrettwilliford/Downloads/fitbit/fitbit_data.xlsx')




def active_data(data):
    sns.lineplot('Date','Minutes Sedentary', data = data)
    sns.lineplot('Date','Minutes Fairly Active', data = data)
    sns.lineplot('Date', 'Minutes Very Active', data = data)
    sns.lineplot('Date', 'Minutes Lightly Active', data = data)
    plt.show()


#subset = data.groupby('Date')['Minutes Sedentary'].mean().reset_index()


#subset = subset.set_index('Date')


#subset = pd.DataFrame(subset['Minutes Sedentary'].resample('W').mean())



def time_predict(data, predict, start_date = '2018-04-26',predict_date ='2018-10-27',info_plots = False, decomp_plot = False, stats_info = False, process_info = False, forecast = False, step_count = 100):
    y = data.groupby('Date')[predict].mean()
    mod = sm.tsa.statespace.SARIMAX(y,
                            order=(1, 1, 1),
                            seasonal_order=(1, 1, 0, 12),
                            enforce_stationarity=False,
                            enforce_invertibility=False)
    results = mod.fit()
    pd.DataFrame(y)
    
    if info_plots:
        results.plot_diagnostics(figsize=(16, 8))
        plt.show()
        
    if decomp_plot:
        decomposition = sm.tsa.seasonal_decompose(y, model='additive')
        fig = decomposition.plot()
        plt.show()
        
    pred = results.get_prediction(start=pd.to_datetime(predict_date), dynamic=False)
    pred_ci = pred.conf_int()

    
    if process_info:
        ax = y[start_date:].plot(label='observed')
        pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
        ax.fill_between(pred_ci.index,
                        pred_ci.iloc[:, 0],
                        pred_ci.iloc[:, 1], color='k', alpha=.2)
        plt.legend()
        plt.show()



    if forecast:
        pred_uc = results.get_forecast(steps=step_count)
        pred_ci = pred_uc.conf_int()
        ax = y.plot(figsize=(14, 7))
        pred_uc.predicted_mean.plot(ax=ax, label='Forecast')
        ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.25)
        plt.legend()
        plt.show()



        
    if stats_info:
        y_forecasted = pred.predicted_mean
        y_truth = y[predict_date:]
        mse = ((y_forecasted - y_truth) ** 2).mean()
        print('<<<<<>>>>><|_STATS_INFO_|><<<<<>>>>>')
        print(results.summary().tables[1])

        


        
    if stats_info:
        y_forecasted = pred.predicted_mean
        y_truth = y[predict_date:]
        mse = ((y_forecasted - y_truth) ** 2).mean()
        print('<<<<<>>>>><|_STATS_INFO_|><<<<<>>>>>')
        print('MSE:  ' + str(mse))
        print('RMSE: ' + str(round(np.sqrt(mse), 2)))

        



def decomp_plot(data, predict, time_series_learn):
    data['date'] = data.index
    y = data.groupby(data['date'])[predict].mean()
    results = time_series_learn.fit()
    decomposition = sm.tsa.seasonal_decompose(y, model='additive')
    results.plot_diagnostics(figsize=(16, 8))
    plt.show()
    fig = decomposition.plot()
    plt.show()




def process_plot(data, predict_value):
    y = data.groupby('Date')[predict_value].mean()
    mod = sm.tsa.statespace.SARIMAX(y,
                            order=(1, 1, 1),
                            seasonal_order=(1, 1, 0, 12),
                            enforce_stationarity=False,
                            enforce_invertibility=False)
    results = mod.fit()
    y = pd.DataFrame(y)
    pred = results.get_prediction(start=pd.to_datetime('2018-10-27'), dynamic=False)
    pred_ci = pred.conf_int()
    ax = y['2018-04-26':].plot(label='observed')
    pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
    ax.fill_between(pred_ci.index,
                        pred_ci.iloc[:, 0],
                        pred_ci.iloc[:, 1], color='k', alpha=.2)
    plt.legend()
    plt.show()



def baseline_model():
    y = data.groupby('Date')[predict_value].mean()
    mod = sm.tsa.statespace.SARIMAX(y,
                            order=(1, 1, 1),
                            seasonal_order=(1, 1, 0, 12),
                            enforce_stationarity=False,
                            enforce_invertibility=False)
    results = mod.fit()
    y = pd.DataFrame(y)
    pred = results.get_prediction(start=pd.to_datetime('2018-10-27'), dynamic=False)
    pred_ci = pred.conf_int()





def forecast_plot(data, predict_value):
    y = data.groupby('Date')[predict_value].mean()
    mod = sm.tsa.statespace.SARIMAX(y,
                            order=(1, 1, 1),
                            seasonal_order=(1, 1, 0, 12),
                            enforce_stationarity=False,
                            enforce_invertibility=False)

    results = mod.fit()
    pred_uc = results.get_forecast(steps=14)
    pred_ci = pred_uc.conf_int()
    y = pd.DataFrame(y)
    ax = y.plot(figsize=(14, 7))
    pred_data = pred_uc.predicted_mean
    
    date_data = (np.array('2018-12-29', dtype = np.datetime64) + np.arange(14))
    
    pred_data['Date'] = date_data
    print(pred_data)
    #print(pred_data)
    #pread_data.plot(label='Forecast')
    #plt.show()
    ##
    
    ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.25)
    plt.legend()
    #plt.show()
    





