import pandas as pd
import os
from sqlalchemy import create_engine
import time
import numpy as np
# 指定要查詢的路徑
yourPath = r'C:/Users/User/Desktop/程式交易系統架構/台股歷史資料(日線)/'

# 列出指定路徑底下所有副檔名為csv的檔案(包含資料夾)
def ListAllFile(path, extension):
    allFileList = os.listdir(path)
    extensionFileList = []
    for item in allFileList:
        try:
            items = item.split('.')
            if items[1] == extension:
                extensionFileList.append(item)
        except:
            continue
    return extensionFileList

def ImportDataToDatabase(FileList):
    for filename in FileList:
        df = pd.read_csv(yourPath + filename, encoding='utf-8')
        
        df = df.replace([np.inf, -np.inf], 0)
        df['日期'] = pd.to_datetime(df['日期'])
        df['成交量'] = df['成交量'].astype(int)
        tableName = filename[:7]

        # #create_engine用來連接sql的url，engine用connect進行連線，
        engine = create_engine("mysql+pymysql://root:h9RR7N5ArSVKf3H2@localhost:3306/程式交易")

        with engine.connect():
            print('-------已成功連上-------')
            # result = engine.execute(query)
            df.to_sql(tableName, engine, index=False, if_exists="append", chunksize=10000)
            print('-------已匯入資料表 {} ---------'.format(tableName))
    return True

FileList = ListAllFile(yourPath, 'csv')
ImportData = ImportDataToDatabase(FileList)











#利用pandas DataFrame寫入
# try:
#     # 連接 MySQL/MariaDB 資料庫
#     connection = mysql.connector.connect(
#         host='localhost',          # 主機名稱
#         database='my_test_db', # 資料庫名稱
#         user='root',        # 帳號
#         password='h9RR7N5ArSVKf3H2')  # 密碼
    
#     if connection.is_connected():

#         # 顯示資料庫版本
#         db_Info = connection.get_server_info()
#         print("資料庫版本：", db_Info)

#         # 顯示目前使用的資料庫
#         cursor = connection.cursor()
        
#         # 創建資料表
#         cursor.execute(sql)
#         print('成功創建: {} 資料表'.format(filename[:7]))
#         time.sleep(3)
#         df.to_sql('{}'.format(filename[:7]), con=connection, if_exists='append')
#         print('成功匯入: {} 資料表'.format(filename[:7]))
#         # cursor.execute(sql3)
#         # print('釋出')
#         # df 匯入到資料表 
#         # df.to_sql(filename[:7], con = connection , if_exists='replace', index = False)

#         # CREATE TABLE `my_test_db`.`tse0050` (`日期` datetime, `開盤` double, `最高` double, `最低` double, `收盤` double, `漲跌` double, `漲跌%` double, `均價5` text, `均價20` text, `均價30` text, `均價60` text, `均價120` text, `成交量` double, `均量5` text, `投信買賣超` int, `投信庫存` int, `自營商買賣` int, `自營商庫存` int, `外資買賣超` int, `外資庫存` int, `布林%b` double, `布林帶寬` double, `MyUnknownColumn` text)

        
#         # cursor.execute("SELECT * FROM my_test_db.0050元大台灣50日線;")
#         # results = cursor.fetchall()
#         # record = cursor.fetchone()
#         # print("目前使用的資料庫：", record)
#         # df = pd.read_sql('SELECT * FROM my_test_db.0050元大台灣50日線', con=connection)
#         # print(df)
        

# except Error as e:
#     print("資料庫連接失敗：", e)

# finally:
#     if (connection.is_connected()):
#         cursor.close()
#         connection.close()
#         print("資料庫連線已關閉")
