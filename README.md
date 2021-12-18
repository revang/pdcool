# kdcool

1. 获取基金成分股信息
2. 获取股票涨跌幅信息（hsudata、tushare）
3. 获取指数行情
4. dataframe函数补充
    - dataframe <---> json
    - dataframe <---> csv
    - dataframe <---> dict
    - show_dataframe
    - series ---> dataframe
    - series <---> dict
    - dataframe <---> excel
5. 添加单元测试


# 参考文档

1. dataframe重命名: https://devnote.pro/posts/10000009321244
2. 

"""

# import pandas as pd
# import json
# inp = [{'c1': 10, 'c2': 100}, {'c1': 11, 'c2': 110}, {'c1': 12, 'c2': 123}]
# df = pd.DataFrame(inp)
# print(df)
# print("______________________________________________")
# # -------------------------按行遍历iterrows():
# for index, row in df.iterrows():
#     print(index)  # 输出每行的索引值
#     print(row['c1'], row['c2'])  # 输出每一行
# print("______________________________________________")
# # -------------------------按列遍历iteritems():
# for index, row in df.iteritems():
#     print(index)  # 输出列名
#     print(row[0], row[1], row[2])  # 输出各列
# print("______________________________________________")
# json_text = df.to_json(orient="records")
# json_data = json.loads(json_text)
# for i in json_data:
#     print(i)
# # print(json_data)

"""