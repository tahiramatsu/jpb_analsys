import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import datetime

st.title("ゆうちょ")

import sys
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError

my_share = share.Share('7182.T')
symbol_data = None

try:
    symbol_data = my_share.get_historical(share.PERIOD_TYPE_YEAR,15,
                                          share.FREQUENCY_TYPE_MONTH,1)
except YahooFinanceError as e:
    print(e.message)
    sys.exit(1)

# print(symbol_data)

# {
#   'timestamp': [...],
#   'open': [...],
#   'high': [...],
#   'low': [...],
#   'close': [...],
#   'adj_close': [...],
#   'volume': [...]
# }

# pandasデータフレームに変換
df = pd.DataFrame(symbol_data)

# タイムスタンプを変換
df["datetime"] = pd.to_datetime(df.timestamp, unit="ms")

# 日本時間へ変換
df["datetime_JST"] = df["datetime"] + datetime.timedelta(hours=9)

st.write(df)

# 日経平均プロファイル　ー日経の指数公式サイトー　より取得
df_index_nikkei = pd.read_csv("nikkei_stock_average_monthly_jp.csv", encoding= "shift_jis")
st.write(df_index_nikkei)