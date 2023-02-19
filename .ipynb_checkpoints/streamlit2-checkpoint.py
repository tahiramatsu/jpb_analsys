import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import datetime

st.title("ゆうちょ")

# 日経平均と銀行業の月次の株価
df_index_nikkei = pd.read_csv("stock_price_monthly_nikkei_bank_yuucho.csv", encoding= "utf-8")

st.write(df_index_nikkei)