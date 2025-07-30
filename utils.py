import pandas as pd
import numpy as np
from datetime import datetime
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA


def arima_model(data,order):
    model = ARIMA(data, order= order)
    arima_fit =  model.fit()

    return arima_fit