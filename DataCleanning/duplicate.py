#程序文件Pex4_26.py
import pandas as pd
a=pd.read_excel("ecommerce.xlsx")
print("是否存在重复观测：",any(a.duplicated()))  #输出：True
a.drop_duplicates(inplace=True)  #inplace=True时，直接删除a中的重复数据
f=pd.ExcelWriter('ecom_results.xlsx')  #创建文件对象
a.to_excel(f)  #把a写入新Excel文件中
f.save()       #保存文件，数据才真正写入Excel文件