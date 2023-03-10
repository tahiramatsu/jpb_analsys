import pandas as pd
# import matplotlib.pyplot as plt
import numpy as np
import datetime
import streamlit as st
# import plotly.express as px

# 日経平均、銀行業、ゆうちょの月次の株価のcsvファイルの読み込み
# 2015‐11‐30を基準点（reference point）として株価を100とする
df_stock_price_yuucho = pd.read_csv("yuucho.csv", encoding= "utf-8")
df_stock_price_yuucho["price"] = df_stock_price_yuucho["price"].str.replace(",","")
df_stock_price_yuucho["price"] = df_stock_price_yuucho["price"].astype(int)
df_stock_price_yuucho['price'] = (df_stock_price_yuucho["price"] - 1740) / 1740
df_stock_price_yuucho.rename(columns={'price': 'yuucho'}, inplace=True)

df_stock_price_yuusei = pd.read_csv("yuusei.csv", encoding= "utf-8")
df_stock_price_yuusei["price"] = df_stock_price_yuusei["price"].str.replace(",","")
df_stock_price_yuusei["price"] = df_stock_price_yuusei["price"].astype(float)
df_stock_price_yuusei['price'] = (df_stock_price_yuusei["price"] - 1907) / 1907
df_stock_price_yuusei.rename(columns={'price': 'yuusei'}, inplace=True)

df_stock_price_kanpo = pd.read_csv("kanpo.csv", encoding= "utf-8")
df_stock_price_kanpo["price"] = df_stock_price_kanpo["price"].str.replace(",","")
df_stock_price_kanpo["price"] = df_stock_price_kanpo["price"].astype(int)
df_stock_price_kanpo['price'] = (df_stock_price_kanpo["price"] - 3360) / 3360
df_stock_price_kanpo.rename(columns={'price': 'kanpo'}, inplace=True)

df_stock_price_bankindex = pd.read_csv("bankindex.csv", encoding= "utf-8")
df_stock_price_bankindex["price"] = df_stock_price_bankindex["price"].astype(float)
df_stock_price_bankindex['price'] = (df_stock_price_bankindex["price"] - 212) / 212
df_stock_price_bankindex.rename(columns={'price': 'bankindex'}, inplace=True)

df_stock_price_nikkeiindex = pd.read_csv("nikkeiindex.csv", encoding= "utf-8")
df_stock_price_nikkeiindex["price"] = df_stock_price_nikkeiindex["price"].str.replace(",","")
df_stock_price_nikkeiindex["price"] = df_stock_price_nikkeiindex["price"].astype(float)
df_stock_price_nikkeiindex['price'] = (df_stock_price_nikkeiindex["price"] - 19747.47) / 19747.47
df_stock_price_nikkeiindex.rename(columns={'price': 'nikkeiindex'}, inplace=True)

df_stock_price_softbankgroup = pd.read_csv("softbankgroup.csv", encoding= "utf-8")
df_stock_price_softbankgroup["price"] = df_stock_price_softbankgroup["price"].str.replace(",","")
df_stock_price_softbankgroup["price"] = df_stock_price_softbankgroup["price"].astype(int)
df_stock_price_softbankgroup['price'] = (df_stock_price_softbankgroup["price"] - 3268) / 3268
df_stock_price_softbankgroup.rename(columns={'price': 'softbankgroup'}, inplace=True)

df_stock_price = pd.merge(df_stock_price_yuucho, df_stock_price_bankindex, on="datetime", how="outer")
df_stock_price = pd.merge(df_stock_price, df_stock_price_kanpo, on="datetime", how="outer")
df_stock_price = pd.merge(df_stock_price, df_stock_price_yuusei, on="datetime", how="outer")
df_stock_price = pd.merge(df_stock_price, df_stock_price_nikkeiindex, on="datetime", how="outer")
df_stock_price = pd.merge(df_stock_price, df_stock_price_softbankgroup, on="datetime", how="outer")
df_stock_price.sort_values(by = 'datetime', ascending = True, inplace = True) 

# 2015‐11‐30を基準点（reference point）として株価を100とする
df_stock_price_rp0 = df_stock_price

st.subheader('１　株価の変動率の推移（2015/11/30基準）と相関係数')
st.caption("ゆうちょ銀行株価（yuucho）　　日本郵政株価（yuusei）")
st.caption("かんぽ株価（kanpo)　　　銀行業インデックス株価（bankindex）")
st.caption("日経平均株価（nikkeiindex)　　　ソフトバンクグループ株価（softbankgroup）")

col1, col2 = st.columns(2)
with col1:
    st.line_chart(df_stock_price_rp0, x="datetime")
    # 株価データの表示のチェックボックス
    if st.checkbox("株価データの表示"):
      df_stock_price
with col2:
    # 相関係数
    df_stock_price.corr = df_stock_price.corr()
    df_stock_price.corr

markdown = """
#### ＜分析結果＞
・基準点（2015年11月30日）と比較すると、日経平均は約30％上昇しているのに対し、ゆうちょ銀行は約30％下落している。
\n
・ゆうちょ銀行、日本郵政、かんぽは、ほぼ同じ株価の推移をとっており、銀行業Indexよりもパフォーマンスが低い。
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
・粗利益に占める割合は、一貫して市場関連が9割で、役務取引等利益（いわゆる手数料ビジネス）は1割程度。
\n
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
・半期毎の市場関連利益のトータルは、約6,000億円から7,000億円程度であり、緩やかな減少傾向にある。
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

st.subheader('４　市場運用利益と評価損益（含み益）の推移')
st.caption("市場運用利益トータル(各期)(total funds balance)　　純利益(Net income)") 
st.caption("評価・換算差額等合計(各期)(Total valuation and translation adjustments)")
st.caption("市場運用利益トータル（累積）＋ 評価・換算差額等合計（各期）(Total valuation and translation adjustments+cumsum(Total funds balance)")
st.line_chart(df_analysis2)
markdown = """
#### ＜分析結果＞
・2016年には約3兆円あった含み益が、2022年9月期にはほぼ0になった。
\n
・実現利益と含み益を考慮すると、6年間で約6兆円（年間1兆円）の利益を市場関連で計上している。
.\n
.\n
.\n
"""
st.write(markdown)

# Total valuation and translation adjustmentsがNaNの行を削除
df_analysis1.dropna(subset=["Total valuation and translation adjustments"], inplace= True)
# df_analysis1["Total valuation and translation adjustments"]

# 2016年3月を評価・換算差額等とcumsum(Total funds balance)の合計
df_analysis1["Total valuation and translation adjustments+cumsum(Total funds balance)"] = df_analysis1["Total valuation and translation adjustments"] +\
df_analysis1["cumsum(Total funds balance)"]

# 2016年3月を評価・換算差額等とcumsum(Total funds balance)の合計0として、変化量をみる
df_analysis1["Total valuation and translation adjustments+cumsum(Total funds balance)"] = (df_analysis1["Total valuation and translation adjustments+cumsum(Total funds balance)"] - (2902894 + 720968)) / (200599151) 

# 日経平均と評価・換算差額等合計のみとするとして、比較表を表示
df_analysis1 = df_analysis1[["nikkei_index", "MSCIworld", "Total valuation and translation adjustments+cumsum(Total funds balance)"]]
# df_analysis1.plot.line()
# plt.show()

st.subheader('５　ゆうちょ市場関連利益、日経平均、MSCIコクサイとの比較')
st.caption("市場運用利益トータル(各期)(total funds balance)")
st.caption("日経平均株価（nikkeiindex)　　　MSCIコクサイ（MSCIworld）")
st.line_chart(df_analysis1)

markdown = """
#### ＜分析結果＞
・ゆうちょの貯金残高は約190兆円前後なので、市場運用利回りは年間0.5％（1兆円/190兆円）程度。
\n
・MSCIコクサイ（日本を除く先進国の株価動向を示す代表的なインデックス）、日経平均と比較するとパフォーマンスが著しく低い。
.\n
.\n
.\n
"""
st.write(markdown)


df_analysis1.corr = df_analysis1.corr()
# df_analysis1.corr
# df_analysis1.corr()


# 日経平均、銀行業、ゆうちょ、MSCIコクサイ、GPIFのcsvファイルの読み込み
df_GPIF_performance = pd.read_csv("GPIF_performance.csv", encoding= "utf-8")

# dateをPandas日付データに変換して昇順にソート
df_GPIF_performance['date'] = pd.to_datetime(df_GPIF_performance['date'], infer_datetime_format= True)
df_GPIF_performance.sort_values(by = 'date', ascending = True, inplace = True) 

# # dateをインデックスに指定
df_GPIF_performance = df_GPIF_performance.set_index("date")
# df_GPIF_performance["GPIF_performance"]
# df_GPIF_performance_rp0 = df_GPIF_performance

df_GPIF_performance = df_GPIF_performance[["GPIF_performance", "yuucho_performance"]]
# df_GPIF_performance.plot.line()
# plt.show()

st.subheader('６　ゆうちょ市場関連利回りとGPIFの利回りとの比較')
st.caption("ゆうちょ市場関連利回り(yuucho_performance)")
st.caption("GPIF利回り（GPIF_performance)")
st.line_chart(df_GPIF_performance)

markdown = """
#### ＜分析結果＞
・GPIF（年金積立金管理運用独立行政法人）と比較すると、ゆうちょは低位安定している。
\n
.\n
.\n
.\n
"""
st.write(markdown)

# 費用分析のcsvファイルの読み込み
df_expense_analysis = pd.read_csv("expense_analysis.csv", encoding= "utf-8")

# dateをPandas日付データに変換して昇順にソート
df_expense_analysis['date'] = pd.to_datetime(df_expense_analysis['date'], infer_datetime_format= True)
df_expense_analysis.sort_values(by = 'date', ascending = True, inplace = True) 

# dateをインデックスに指定
df_expense_analysis = df_expense_analysis.set_index("date")
# df_expense_analysis

# df_expense_analysis[["Personnel expenses","G total", "Non-personnel expenses(others)", "Taxes and dues"]].plot(kind="line")
df_expense_analysis_c = df_expense_analysis[["Personnel expenses","G total", "Non-personnel expenses(others)", "Taxes and dues"]]

st.subheader('７　ゆうちょ費用構造')
st.caption("日本郵便への委託手数料、郵政管理・支援機構への拠出金(G total)")
st.caption("人件費(Personnel expenses) ")
st.caption("その他(Non-personnel expenses(others)　　税金(Taxes and dues))")
st.area_chart(df_expense_analysis_c)

markdown = """
#### ＜分析結果＞
・費用の６割以上は日本郵便、郵政管理・支援機構へ支払金。
\n
・人件費、システム費用は、それぞれ15％程度。
\n
.\n
.\n
.\n
"""
st.write(markdown)

df_expense_analysis["employee"] = (df_expense_analysis["employee"] - 18878) / 18878
df_expense_analysis["employee in branch"] = (df_expense_analysis["employee in branch"] - 5411) / 5411
# df_expense_analysis[["employee", "employee in branch"]].plot.line()
df_expense_analysis_a = df_expense_analysis[["employee", "employee in branch"]]

st.subheader('８　ゆうちょ人員数の推移')
st.caption("総人員数(employee)")
st.caption("店舗人員数(employee in branch) ")
st.line_chart(df_expense_analysis_a)

markdown = """
#### ＜分析結果＞
・総人員数は緩やかに減っているが、店舗人員数は過去4年で大幅に減少。
\n
\n
.\n
.\n
.\n
"""
st.write(markdown)

df_expense_analysis["Personnel expenses"] = (df_expense_analysis["Personnel expenses"] - 1220) / 1220 
# df_expense_analysis[["employee", "Personnel expenses"]].plot.line()
df_expense_analysis_b = df_expense_analysis[["employee", "Personnel expenses"]]

st.subheader('９　ゆうちょ人員数と人件費の推移')
st.caption("総人員数(employee)")
st.caption("人件費(Personnel expenses) ")
st.line_chart(df_expense_analysis_b)

markdown = """
#### ＜分析結果＞
・総人員数の減少率と比較して人件費は減少していない。
\n
\n
.\n
.\n
.\n
"""
st.write(markdown)

df_expense_analysis["G total"] = (df_expense_analysis["G total"] - 6213) / 6213
# df_expense_analysis[["G total", "employee in branch"]].plot(kind="line")
df_expense_analysis_c = df_expense_analysis[["G total", "employee in branch"]]

st.subheader('１０　店舗人員数との推移')
st.caption("店舗人員数(e日本郵便、郵政管理・支援機構へ支払金mployee in branch)")
st.caption("(G total) ")
st.line_chart(df_expense_analysis_c)

markdown = """
#### ＜分析結果＞
・店舗総人員は減少しているが、日本郵便、郵政管理・支援機構へ支払金は減少していない。
\n
\n
.\n
.\n
.\n
"""
st.write(markdown)

# df_yuucho_factbook1[["Gross operating profit","Net fees and commissions"]].plot(kind="line")
# st.area_chart(df_profit_analysis_a)

