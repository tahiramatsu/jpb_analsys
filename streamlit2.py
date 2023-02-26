import pandas as pd
# import matplotlib.pyplot as plt
import numpy as np
import datetime
import streamlit as st
import plotly.express as px

# st.title("ゆうちょ")

# 日経平均、銀行業、ゆうちょの月次の株価のcsvファイルの読み込み
df_stock_price = pd.read_csv("stock_price_monthly_nikkei_bank_yuucho.csv", encoding= "utf-8")

# dayをPandas日付データに変換して昇順にソート
df_stock_price['date'] = pd.to_datetime(df_stock_price['date'], infer_datetime_format= True)
df_stock_price.sort_values(by = 'date', ascending = True, inplace = True) 

# # dayをインデックスに指定
df_stock_price = df_stock_price.set_index("date")

# 2015‐11‐30を基準点（reference point）として株価を100とする
df_stock_price_rp0 = df_stock_price
df_stock_price_rp0["nikkei_index"]  = (df_stock_price_rp0["nikkei_index"] - 19747) / 19747
df_stock_price_rp0["bank_index"] = (df_stock_price_rp0["bank_index"] - 212) / 212
df_stock_price_rp0["yuucho"] = (df_stock_price_rp0["yuucho"] - 1740) / 1740
df_stock_price_rp0["SBG"] = (df_stock_price_rp0["SBG"] - 3268) / 3268

# グラフ化（plt）
# df_stock_price_rp0.plot(kind="line")
# グラフ化（px）
# px.line(df_stock_price_rp0, x="day", y="yuucho", color="stock_name", markers=True)
# グラフ化（st）
st.subheader('１　株価の変動率の推移（2015/11/30基準）と相関係数')
st.caption("日経平均株価（nikkei_index)　　　銀行業インデックス株価（bank_index）")
st.caption("ゆうちょ銀行株価（yuucho）　　ソフトバンクグループ株価（SBG）")

# st.line_chart(df_stock_price_rp0)

# # 相関係数
# # st.subheader('株価間の相関係数')
# df_stock_price.corr = df_stock_price.corr()
# # df_stock_price.corr
# # df_stock_price.corr()


col1, col2 = st.columns(2)
with col1:
    st.line_chart(df_stock_price_rp0)
    # 株価データの表示のチェックボックス
    if st.checkbox("株価データの表示"):
      df_stock_price
with col2:
    # 相関係数
    df_stock_price.corr = df_stock_price.corr()
    df_stock_price.corr

markdown = """
#### ＜分析結果＞
・gaga
\n
・gaga
\n
・不祥事案1　 2019年6月14日：投資信託を不適切販売
\n
・不祥事案2　 2020年9月25日：キャッシュレス決済の不正送金
\n
.\n
.\n
.\n
"""
st.write(markdown)

# ゆうちょfactbook1の読み込み(Income Analysis (Non-consolidated))
df_yuucho_factbook1 = pd.read_csv("yuucho_factbook1.csv", encoding= "utf-8")

# 日付をPandas日付データに変換して昇順にソート
df_yuucho_factbook1["date"] = pd.to_datetime(df_yuucho_factbook1["date"], infer_datetime_format= True)
df_yuucho_factbook1.sort_values(by = "date", ascending = True, inplace = True) 

# dateをインデックスに指定
df_yuucho_factbook1 = df_yuucho_factbook1.set_index("date")
# df_yuucho_factbook1

# ゆうちょfactbook2の読み込み(Summarized Balance Sheets (Non-consolidated))
df_yuucho_factbook2 = pd.read_csv("yuucho_factbook2.csv", encoding= "utf-8")

# 日付をPandas日付データに変換して昇順にソート
df_yuucho_factbook2["date"] = pd.to_datetime(df_yuucho_factbook2["date"], infer_datetime_format= True)
df_yuucho_factbook2.sort_values(by = "date", ascending = True, inplace = True) 

# dateをインデックスに指定
df_yuucho_factbook2 = df_yuucho_factbook2.set_index("date")
# df_yuucho_factbook2

# NaNを0に変換
df_yuucho_factbook1.fillna(0, inplace=True)

# 資金利益、外国為替売買損益、国債等債券損益、株式等関係損益、金銭の信託運用損益、減損損失の合計、当期純利益を表示
df_yuucho_factbook1["Total funds balance"] = df_yuucho_factbook1["Net interest income"] + df_yuucho_factbook1["Gains (losses) on foreign exchanges"]\
+ df_yuucho_factbook1["Gains (losses) on bonds"] + df_yuucho_factbook1["Gains (losses) related to stocks"]\
+ df_yuucho_factbook1["Gains (losses) on money held in trust"] + df_yuucho_factbook1["Losses on impairment of fixed assets"]
# df_yuucho_factbook1[["Net interest income", "Gains (losses) on foreign exchanges", "Gains (losses) on bonds", \
#                     "Gains (losses) related to stocks", "Gains (losses) on money held in trust", "Losses on impairment of fixed assets",\
#                     "Total funds balance", "Net income"]].plot(kind="line")
# df_yuucho_factbook1

st.subheader('２　粗利益の推移')
st.caption("資金利益（Net fees and commissions）　　役務取引等利益(Net fees and commissions)") 
st.caption("その他業務利益(Net other operating income (loss)")
df_profit_analysis_a = df_yuucho_factbook1[["Net interest income","Net fees and commissions", "Net other operating income (loss)"]]
st.area_chart(df_profit_analysis_a)
markdown = """
#### ＜分析結果＞
・gaga
\n
・gaga
\n
・不祥事案1　 2019年6月14日：投資信託を不適切販売
\n
・不祥事案2　 2020年9月25日：キャッシュレス決済の不正送金
\n
.\n
.\n
.\n
"""
st.write(markdown)




st.subheader('３　市場運用利益の推移')
st.caption("市場運用利益トータル（Total funds balance)　　　資金利益（Net intest income）")
df_yuucho_factbook1 = df_yuucho_factbook1[["Net interest income", "Gains (losses) on foreign exchanges", "Gains (losses) on bonds", \
                    "Gains (losses) related to stocks", "Gains (losses) on money held in trust", "Losses on impairment of fixed assets",\
                    "Total funds balance", "Net income"]]
st.line_chart(df_yuucho_factbook1)

# 株価データの表示のチェックボックス
if st.checkbox("市場運用利益データの表示"):
    df_yuucho_factbook1

markdown = """
#### ＜分析結果＞
・gaga
\n
・gaga
\n
・不祥事案1　 2019年6月14日：投資信託を不適切販売
\n
・不祥事案2　 2020年9月25日：キャッシュレス決済の不正送金
\n
.\n
.\n
.\n
"""
st.write(markdown)

# 日経平均、銀行業、ゆうちょ、MSCIコクサイのcsvファイルの読み込み
df_stock_price_MSCIworld = pd.read_csv("stock_price_MSCIworld.csv", encoding= "utf-8")

# dateをPandas日付データに変換して昇順にソート
df_stock_price_MSCIworld['date'] = pd.to_datetime(df_stock_price_MSCIworld['date'], infer_datetime_format= True)
df_stock_price_MSCIworld.sort_values(by = 'date', ascending = True, inplace = True) 

# # dateをインデックスに指定
df_stock_price_MSCIworld = df_stock_price_MSCIworld.set_index("date")
# df_stock_price_MSCIworld
df_stock_price_MSCIworld_rp0 = df_stock_price_MSCIworld

# 2016‐03‐31を基準点（reference point）として株価を100とする
df_stock_price_MSCIworld_rp0["nikkei_index"]  = (df_stock_price_MSCIworld_rp0["nikkei_index"] - 16759) / 16759
df_stock_price_MSCIworld_rp0["bank_index"] = (df_stock_price_MSCIworld_rp0["bank_index"] - 146) / 146
df_stock_price_MSCIworld_rp0["yuucho"] = (df_stock_price_MSCIworld_rp0["yuucho"] - 1385) / 1385
df_stock_price_MSCIworld_rp0["MSCIworld"] = (df_stock_price_MSCIworld_rp0["MSCIworld"] - 7503) / 7503

# df_stock_price_MSCIworld["bank_index"] = df_stock_price_MSCIworld["bank_index"]*(16759 / 146)
# df_stock_price_MSCIworld["yuucho"] = df_stock_price_MSCIworld["yuucho"]*(16759 / 1385)
# df_stock_price_MSCIworld_rp0["MSCIworld"] = df_stock_price_MSCIworld_rp0["MSCIworld"]*(16759 / 7503)

# df_stock_price_MSCIworld_rp0.plot(kind="line")
# st.line_chart(df_stock_price_MSCIworld_rp0)

# 分析用に_MSCIworldとdf_yuucho_factbook1とdf_yuucho_factbook2結合
df_analysis1 = df_stock_price_MSCIworld.join(df_yuucho_factbook1)
df_analysis1 = df_analysis1.join(df_yuucho_factbook2)
# df_analysis1

# 2016年3月を評価・換算差額等とTotal funds balanceの合計
df_analysis1["Total valuation and translation adjustments+Total funds balance"] = df_analysis1["Total valuation and translation adjustments"] +\
df_analysis1["Total funds balance"]
# df_analysis1["Total valuation and translation adjustments＋Total funds balance"] 

# Total funds balanceの累積和
df_analysis1["cumsum(Total funds balance)"] = df_analysis1["Total funds balance"].cumsum()
# df_analysis1["cumsum(Total funds balance)"]

# 2016年3月を評価・換算差額等とcumsum(Total funds balance)の合計
df_analysis1["Total valuation and translation adjustments+cumsum(Total funds balance)"] = df_analysis1["Total valuation and translation adjustments"] +\
df_analysis1["cumsum(Total funds balance)"]

# Total funds balanceとNet incomeと評価・換算差額等合計のみとして、比較表を表示
df_analysis2 = df_analysis1[["Total funds balance", "Net income", "Total valuation and translation adjustments", "Total valuation and translation adjustments+cumsum(Total funds balance)"]]
# df_analysis2.plot.line(subplots=True) 
# df_analysis2.plot.line()
# plt.show()

st.subheader('３　市場運用利益と評価損益（含み益）の推移')
st.caption("市場運用利益トータル(各期)(total funds balance)　　純利益(Net income)") 
st.caption("評価・換算差額等合計(各期)(Total valuation and translation adjustments)")
st.caption("市場運用利益トータル（累積）＋ 評価・換算差額等合計（各期）(Total valuation and translation adjustments+cumsum(Total funds balance)")
st.line_chart(df_analysis2)
markdown = """
#### ＜分析結果＞
・gaga
\n
・gaga
\n
・不祥事案1　 2019年6月14日：投資信託を不適切販売
\n
・不祥事案2　 2020年9月25日：キャッシュレス決済の不正送金
\n
.\n
.\n
.\n
"""
st.write(markdown)

# Total valuation and translation adjustmentsがNaNの行を削除
df_analysis1.dropna(subset=["Total valuation and translation adjustments"], inplace= True)
df_analysis1["Total valuation and translation adjustments"]

# 2016年3月を評価・換算差額等とcumsum(Total funds balance)の合計
df_analysis1["Total valuation and translation adjustments+cumsum(Total funds balance)"] = df_analysis1["Total valuation and translation adjustments"] +\
df_analysis1["cumsum(Total funds balance)"]

# 2016年3月を評価・換算差額等とcumsum(Total funds balance)の合計0として、変化量をみる
df_analysis1["Total valuation and translation adjustments+cumsum(Total funds balance)"] = (df_analysis1["Total valuation and translation adjustments+cumsum(Total funds balance)"] - (2902894 + 720968)) / (200599151) 

# 日経平均と評価・換算差額等合計のみとするとして、比較表を表示
df_analysis1 = df_analysis1[["nikkei_index", "MSCIworld", "Total valuation and translation adjustments+cumsum(Total funds balance)"]]
# df_analysis1.plot.line()
# plt.show()
st.line_chart(df_analysis1)

df_analysis1.corr = df_analysis1.corr()
df_analysis1.corr
# df_analysis1.corr()


# 日経平均、銀行業、ゆうちょ、MSCIコクサイ、GPIFのcsvファイルの読み込み
df_GPIF_performance = pd.read_csv("GPIF_performance.csv", encoding= "utf-8")

# dateをPandas日付データに変換して昇順にソート
df_GPIF_performance['date'] = pd.to_datetime(df_GPIF_performance['date'], infer_datetime_format= True)
df_GPIF_performance.sort_values(by = 'date', ascending = True, inplace = True) 

# # dateをインデックスに指定
df_GPIF_performance = df_GPIF_performance.set_index("date")
df_GPIF_performance["GPIF_performance"]
# df_GPIF_performance_rp0 = df_GPIF_performance

df_GPIF_performance = df_GPIF_performance[["GPIF_performance", "yuucho_performance"]]
# df_GPIF_performance.plot.line()
# plt.show()
st.line_chart(df_GPIF_performance)


# 費用分析のcsvファイルの読み込み
df_expense_analysis = pd.read_csv("expense_analysis.csv", encoding= "utf-8")

# dateをPandas日付データに変換して昇順にソート
df_expense_analysis['date'] = pd.to_datetime(df_expense_analysis['date'], infer_datetime_format= True)
df_expense_analysis.sort_values(by = 'date', ascending = True, inplace = True) 

# dateをインデックスに指定
df_expense_analysis = df_expense_analysis.set_index("date")
df_expense_analysis

# df_expense_analysis[["Personnel expenses","G total", "Non-personnel expenses(others)", "Taxes and dues"]].plot(kind="line")
df_expense_analysis_c = df_expense_analysis[["Personnel expenses","G total", "Non-personnel expenses(others)", "Taxes and dues"]]
st.area_chart(df_expense_analysis_c)

df_expense_analysis["employee"] = (df_expense_analysis["employee"] - 18878) / 18878
df_expense_analysis["employee in branch"] = (df_expense_analysis["employee in branch"] - 5411) / 5411
# df_expense_analysis[["employee", "employee in branch"]].plot.line()
df_expense_analysis_a = df_expense_analysis[["employee", "employee in branch"]]
st.line_chart(df_expense_analysis_a)

df_expense_analysis["Personnel expenses"] = (df_expense_analysis["Personnel expenses"] - 1220) / 1220 
# df_expense_analysis[["employee", "Personnel expenses"]].plot.line()
df_expense_analysis_b = df_expense_analysis[["employee", "Personnel expenses"]]
st.line_chart(df_expense_analysis_b)

df_expense_analysis["G total"] = (df_expense_analysis["G total"] - 6213) / 6213
# df_expense_analysis[["G total", "employee in branch"]].plot(kind="line")
df_expense_analysis_c = df_expense_analysis[["G total", "employee in branch"]]
st.line_chart(df_expense_analysis_c)

# df_yuucho_factbook1[["Gross operating profit","Net fees and commissions"]].plot(kind="line")
# st.area_chart(df_profit_analysis_a)

