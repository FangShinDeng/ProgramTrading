import pandas as pd
import mysql.connector
from mysql.connector import Error
from sqlalchemy import create_engine

# 先將單一資料表匯入資料庫
filename = 'tse0050.csv'
tableName = filename[:7]

# 讀取csv file
df = pd.read_csv(filename, encoding='utf-8')

# 數據格式修正
df['Date'] = pd.to_datetime(df['Date'])

# 使用sqlalchemy創建資料庫連線 #create_engine用來連接sql的url，engine用connect進行連線，
engine = create_engine("mysql+pymysql://root:h9RR7N5ArSVKf3H2@localhost:3306/my_test_db")

with engine.connect() as connection:
    print('-------已成功連上-------')
    # result = engine.execute(query)
    df.to_sql(tableName, engine, index=False, if_exists="replace", chunksize=10000)
    print('-------已匯入資料表 {} ---------'.format(tableName))

    AllRecords = engine.execute("SELECT * FROM {}".format(tableName)).fetchall()
    print(AllRecords)
