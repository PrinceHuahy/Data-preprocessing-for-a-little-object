import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
for i in range(366):
    house = pd.read_csv(r"C:/Users/Khan/Documents/all/beijing_all_1 ("+str(1)+").csv")  #括号里填入文件地址
    for col in house.columns: #删除全为nan的列
        if house[col].isnull().sum() == len(house[col]):
            del house[col]
        for row in range(house.shape[0]):  # 这个循环的作用是删除全为nan的行
            if house.loc[row, :].isnull().sum() > 10:  # 这里的10是一个超参数，当每行的缺失值个数超过十个时会将这一行删除
                house = house.drop([row])
        for col in house.columns[3:]:  # 将个别的缺失值用平均值进行填充
            col = house.loc[:, col].values.reshape(-1, 1)  # sklearn中的矩阵必须是二维
            imp_mean = SimpleImputer()
            imp_mean = imp_mean.fit_transform(col)
        house = house.sort_values(by=['type'], ascending=False)  # 排序
        out_path = "D:/数据/Beijing" + str(i) + ".csv"
        house.to_csv(out_path, sep=",", index=True, header=True)





