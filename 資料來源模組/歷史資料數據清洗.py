import pandas as pd
import os
import time
import numpy as np
yourPath = r'C:/Users/User/Desktop/DataSource/台股歷史資料(日線)/整理後/'

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
    print(extensionFileList)
    return extensionFileList

# 清除欄位，修改日期格式
def DataClear(FileList):
    for filename in FileList:

        df = pd.read_csv(yourPath + '{}'.format(filename), encoding='big5')
        df = df.replace([np.inf, -np.inf], np.nan)
        # 去除欄位空白問題,修改日期格式,成交量格式
        df = df.rename(columns={
            ' 成交量':'Volume',
            '日期':'Date',
            '開盤':'Open',
            '最高':'High',
            '最低':'Low',
            '收盤': 'Close',
            '漲跌': 'Change',
            '漲跌%': 'ChangePCT'})
        
        df['Date'] = pd.to_datetime(df['Date'])
        df['Volume'] = df['Volume'].astype(int)
        # 去除最後一欄unamed:22
        df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Change', 'ChangePCT', 'Volume']]
        
        # 將所有df的小數點取到第二位
        df= df.round(2)
        # print(df.dtypes)
        # print(df)
        
        print('-----已更新 {} 資料表-----'.format(filename))
        df.to_csv(filename, encoding = 'utf-8', index = False)

FileList = ListAllFile(yourPath, 'csv')
DataClear(FileList)