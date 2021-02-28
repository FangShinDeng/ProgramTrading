import pandas as pd
import os
import time
import numpy as np
yourPath = r'C:/Users/User/Desktop/程式交易系統架構/台股歷史資料(日線)/'

# 列出指定路徑底下所有副檔名為csv的檔案(包含資料夾)
def ListAllFile(path, extension):
    allFileList = os.listdir(yourPath)
    extensionFileList = []
    for item in allFileList:
        try:
            items = item.split('.')
            if items[1] == extension:
                extensionFileList.append(item)
        except:
            continue
    return extensionFileList

# 清除欄位，修改日期格式
def DataClear(FileList):
    for filename in FileList:

        df = pd.read_csv(yourPath + '{}'.format(filename), encoding='big5')
        df = df.replace([np.inf, -np.inf], np.nan)
        # 去除欄位空白問題,修改日期格式,成交量格式
        df = df.rename(columns={' 成交量':'成交量'})
        
        df['日期'] = pd.to_datetime(df['日期'])
        df['成交量'] = df['成交量'].astype(int)
        # 去除最後一欄unamed:22
        df = df[['日期', '開盤', '最高', '最低', '收盤', '漲跌', '漲跌%', '成交量']]

        # print(df.dtypes)
        # print(df)
        
        print('-----已更新 {} 資料表-----'.format(filename))
        df.to_csv(filename, encoding = 'utf-8', index = False)

FileList = ListAllFile(yourPath, 'csv')
DataClear(FileList)