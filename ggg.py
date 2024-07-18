import pandas as pd
import tushare as ts
token = '292bb07649df4e61c82c6cce9a32c66cf250bc95bf04a300f4960d03'
ts.set_token(token)
pro = ts.pro_api()
df = pro.daily_basic(ts_code='', trade_date='20240624', fields='ts_code,trade_date,turnover_rate,volume_ratio,pe,pb,total_mv')
#df = pd.read_csv(r'D:\Download\交易软件\客户端\client_test_516_20240618_C\database\所需数据.csv')

print(df)
df.to_csv(r'D:\Download\交易软件\客户端\client_test_516_20240618_C\database\股票代码.csv')
