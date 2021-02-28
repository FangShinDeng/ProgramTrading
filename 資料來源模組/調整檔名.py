import os

# 指定要查詢的路徑

yourPath = r'C:/Users/User/Desktop/程式交易系統架構/台股歷史資料(日線)'

# 列出指定路徑底下所有檔案(包含資料夾)
allFileList = os.listdir(yourPath)
# print(allFileList)

# 讀取前面4位的股號，並記錄起來
stockList = []
for item in allFileList:
    oldname = item
    newname = 'TSE' + item[:4] + '.csv'
    os.rename(oldname, newname)

    stockList.append(newname)

stockList = stockList[:-3]
print(stockList)
