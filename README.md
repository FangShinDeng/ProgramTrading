# 用Python搭建程式交易回測系統及自動化交易
    今天是2021/2/22，決定要開始搭建自己的交易回測系統及自動化交易
    目標: 用完整系統架構的方式完成相對低相對高的自動化交易策略，並且達成日後開發新策略時能更有模組化的去進行開發
    依照我的策略我將分成3個階段
    1. 每日自動化產出股票投資清單，供檢視
    2. 開發自動化優化參數程式，能調整程式中的所有參數，並優化得出最佳報酬的參數
    3. 使用永豐金API開發完畢自動化交易的程式

# 回測交易系統架構
    參考連結: https://ithelp.ithome.com.tw/articles/10226516?sc=rss.iron
    依照上述參考連結來完成以下5點模組的開發
    1. 資料來源模組
    2. 時序運行模組
    3. 策略運行模組
    4. 交易執行模組
    5. 交易統計模組

# 資料來源模組
    資料來源，又分成兩種
    1. 歷史資料: 採用爬蟲或其他第三方平台或軟件去獲取
        a. 股票
            用永豐API去抓歷史資料，只能抓到近3年的歷史資料
            但因為我的朋友平常有收集資料的習慣，因此我先將它提供給我的所有歷史資料匯入後，在去用API每日更新數據即可
        b. 期貨
        c. 外匯資料, 下載MT5軟體，然後在商品的功能去下載需要的分K或是逐筆交易資料
        
    2. 即時資料: 採用永豐API的資料

    ## 程式清單
    永豐API獲取股票清單.py: 用來產出4個股號的股票清單
    調整檔名.py: 將檔名改為標準格式 '0050.csv' -> 'TSE0050.csv'
    單表匯入歷史資料進資料庫.py: 將指定的資料表匯入到MySQL資料庫
    批量匯入歷史資料進資料庫.py: 將資料夾中的所有資料表匯入到MySQL資料庫
    歷史資料數據清洗.py: 將資料格式整理好(dtypes), 去除不必要的欄位及空白
    永豐API更新股票資料.py: 將每日台股的日線資料更新至資料庫

## 用df直接匯入MySQL資料庫
    參考連結: https://medium.com/sq-catch-and-note/python-%E4%BD%BF%E7%94%A8sqlalchemy%E8%88%87pandas%E8%AE%80%E5%AF%AB%E8%B3%87%E6%96%99%E5%BA%AB-3a61ad7a881a
    
    關於什麼是 ORM 框架？
    參考連結: https://www.maxlist.xyz/2019/10/30/flask-sqlalchemy/
    簡單來說是直接用 Python 的語法對資料庫進行操作，不需要直接寫 SQL 語法，ORM 背後會自動將 Python 代碼轉換成應對的 SQL 語法，再來進行對資料庫的操作。
    – 優點： 可讀性較高，也可以防止 SQL injection
    – 缺點： 因為多了一層 python 的包裝會犧牲掉部分的效能