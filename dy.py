import pandas as pd
import re

df = pd.read_csv('D:/wenben/gov_reports.csv')
df.head()

df['year'] = df['file'].apply(lambda f: re.findall('\d{4}', f)[0])
df['prov'] = df['file'].apply(lambda f: re.findall('/(.*?)/', f)[0]) 
df.head()



table_df = pd.pivot_table(df, 
                       columns='year',  #列-年份
                       index='prov',    #行-省份
                       values='text',   #单元格-文本
                       aggfunc=lambda cs: ''.join(str(c) for c in cs)) #让单元格填充文本

table_df
pip install numpy==1.19.5


import pandas as pd

# 假设你已经创建了 table_df 数据框

# 保存为 Excel 文件
import pandas as pd
import numpy as np
np.float = float

# 假设你已经创建了 table_df 数据框

# 保存为 Excel 文件
table_df.to_excel('table_data.xlsx')  # 设置 index=True 可以将行索引保存为列




pip install --upgrade scikit-learn