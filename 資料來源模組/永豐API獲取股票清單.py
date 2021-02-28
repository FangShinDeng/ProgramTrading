# 登入
import shioaji as sj
import datetime
import pandas as pd
import requests
api = sj.Shioaji()
accounts = api.login("身分證字號", "密碼")
ca = api.activate_ca(
    ca_path="C:/ekey/551/身分證字號/S/Sinopac.pfx",
    ca_passwd="身分證字號",
    person_id="身分證字號",
)

# 所有股票合約清單
AllStocks = api.Contracts.Stocks['TSE']
StockList = []

# 抓出代碼是4位的所有股票
for stock in AllStocks:
    if len(stock.code) == 4:
#         print(stock)
        StockList.append(dict(stock))

stockDf = pd.DataFrame(StockList) # 股票清單 Df
stockList = stockDf.code.tolist() # 股票清單 List
stockDf.to_csv('台股股票清單.csv', encoding = 'utf-8')
print(stockDf.code)