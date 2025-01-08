import csv
import pandas as pd
import numpy as np
ServerURL = 'https://class.iottalk.tw' #For example: 'https://DomainName'
MQTT_broker = 'iot.iottalk.tw' # MQTT Broker address, for example: 'DomainName' or None = no MQTT support
MQTT_port = 8883
MQTT_encryption = True
MQTT_User = 'iottalk'
MQTT_PW = 'iottalk2023'

device_model = 'Dummy_Device'
IDF_list = ['Dummy_Sensor']
ODF_list = ['Dummy_Control']
device_id = 'midterm_demo' #if None, device_id = MAC address
device_name = 'midterm_demo'
exec_interval = 1  # IDF/ODF interval


def on_register(r):
    print(f'Device name: {r["d_name"]}')

count=1
oneData=[]
datalist=[]
light = 50

def Dummy_Sensor():
    global light

    return light


"""for 收集資料"""
count_for_dictwriter=1
"""for 收集資料"""

# 選擇訓練好的模型
import pickle

# model_pkl_file = 'random_forest_model.pkl'
model_pkl_file = 'svm_rbf_model.pkl'

with open(model_pkl_file, 'rb') as file:  
    model = pickle.load(file)
file.close()

# 模型function  
def ml_predict(inputData):
    
    result=model.predict(inputData)
    # print("result",result)  #1,2
    return result

def Dummy_Control(data:list):

    '''"""for 收集資料 begin"""

    """
    將sensor寫檔
    寫檔用任何一種方法均可
    """
    name1='vertical.csv'
    name2='horizontal.csv'
    with open(name2,'a',newline='') as file:
        # 將dictionary 寫入 csv檔
        writer=csv.DictWriter(file,['acc1','acc2','acc3','gyro1','gyro2','gyro3'])
        # 寫入第一列的欄位名稱
        # writer.writeheader()

        global count_for_dictwriter
        print("-----  count  =  ",count_for_dictwriter)
        print(data[0][0],data[0][1],data[0][2],data[0][3],data[0][4],data[0][5])
        if(count_for_dictwriter%10==0):
            print("收集完第",count_for_dictwriter//10,"組資料(每一組資料含10筆，一筆有6個數值)")
        else:
            print("收集",count_for_dictwriter%10,"/10 ......")
    
        writer.writerow({'acc1':data[0][0],'acc2':data[0][1],'acc3':data[0][2],'gyro1':data[0][3],'gyro2':data[0][4],'gyro3':data[0][5]})

        count_for_dictwriter=count_for_dictwriter+1
        print("==========")
    """for 收集資料 end"""'''

    """for inference begin"""
    global count
    global oneData
    global datalist
    global light

    if count % 10 != 0 and count !=0:
        print("正在收集",count,"/10資料")
        oneData=[data[0][0],data[0][1],data[0][2],data[0][3],data[0][4],data[0][5]]
        datalist.append(oneData)
        count+=1
    else:
        oneData=[data[0][0],data[0][1],data[0][2],data[0][3],data[0][4],data[0][5]]
        datalist.append(oneData)
        print("收集完一單位資料(60個數值)--------------------")
        count=1
        oneData=[]
        
        #一定要加這一行 reshape把資料變成一格陣列
        datalist=pd.DataFrame(np.array(datalist).reshape(1,-1),columns=['acc1_1','acc2_1','acc3_1','gyro1_1','gyro2_1','gyro3_1','acc1_2','acc2_2','acc3_2','gyro1_2','gyro2_2','gyro3_2','acc1_3','acc2_3','acc3_3','gyro1_3','gyro2_3','gyro3_3','acc1_4','acc2_4','acc3_4','gyro1_4','gyro2_4','gyro3_4','acc1_5','acc2_5','acc3_5','gyro1_5','gyro2_5','gyro3_5','acc1_6','acc2_6','acc3_6','gyro1_6','gyro2_6','gyro3_6','acc1_7','acc2_7','acc3_7','gyro1_7','gyro2_7','gyro3_7','acc1_8','acc2_8','acc3_8','gyro1_8','gyro2_8','gyro3_8','acc1_9','acc2_9','acc3_9','gyro1_9','gyro2_9','gyro3_9','acc1_10','acc2_10','acc3_10','gyro1_10','gyro2_10','gyro3_10'])
        #用模型判斷 #可能這裡的datalist要在處理一下轉成model可以訓練一筆的格式
        predictResult=ml_predict(datalist)  
        #print(predictResult)
        print("-----手勢偵測結果-----")
        if predictResult==1:
            print("偵測到垂直，燈泡亮度變最亮\n")
            light=100
        elif predictResult==2:    
            print("偵測到水平，燈泡亮度變最暗\n")
            light=0
        else:
            print("不知道你在做啥，燈泡亮度中間值\n")
            light=50

        datalist=[]
        # print("現在亮度為=",light)
        print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
"""for inference end"""
