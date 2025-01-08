"""
先把10筆(1筆包含6個數值)資料串成一列

combine.csv
每一列60個數值，共200列(o.csv,x.csv各100列)
最後加上label(o:1,x:2)

"""

import csv
import os

rowInTen=[]#存一列60個數值
datas=[]#存100列rowInTen
count=0

# o.csv -> label = [1], x.csv -> label = [2]
name1='vertical.csv'
name2='horizontal.csv'
label = [2]

with open(name2) as file:
    data=csv.reader(file)#使用csv.reader讀出來的的資料是list
    for row in data:
        #每10筆換一行
        if count%10==0 and count!=0:    
            datas.append(rowInTen + label)   #append:向列表尾部添加新元素 ，但這裡是把list串到list中  先把之前rowInTen的資料append到datas  append用法前面不須賦值
            rowInTen=[] #再把rowInTen清空
            rowInTen=rowInTen+row        
            count+=1
        else:
            rowInTen=rowInTen+row   #這樣寫是list串接
            count+=1

#print(type(datas))#list
print(len(datas))
#寫檔combine.csv
for i in datas:
    #開啟輸出的 CSV 檔案
    with open('combine2.csv','a',newline='') as csvfile:
        #建立 CSV 檔寫入器
        writer=csv.writer(csvfile)
        if os.stat('combine2.csv').st_size == 0:
            writer.writerow(['acc1_1','acc2_1','acc3_1','gyro1_1','gyro2_1','gyro3_1','acc1_2','acc2_2','acc3_2','gyro1_2','gyro2_2','gyro3_2','acc1_3','acc2_3','acc3_3','gyro1_3','gyro2_3','gyro3_3','acc1_4','acc2_4','acc3_4','gyro1_4','gyro2_4','gyro3_4','acc1_5','acc2_5','acc3_5','gyro1_5','gyro2_5','gyro3_5','acc1_6','acc2_6','acc3_6','gyro1_6','gyro2_6','gyro3_6','acc1_7','acc2_7','acc3_7','gyro1_7','gyro2_7','gyro3_7','acc1_8','acc2_8','acc3_8','gyro1_8','gyro2_8','gyro3_8','acc1_9','acc2_9','acc3_9','gyro1_9','gyro2_9','gyro3_9','acc1_10','acc2_10','acc3_10','gyro1_10','gyro2_10','gyro3_10','label'])
        #寫入一列資料
        writer.writerow(i)
