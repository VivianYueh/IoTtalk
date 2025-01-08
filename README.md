# IoTtalk_final_project

## 一、專案內容

透過智慧手機輸入手勢資料，並由Dummy Device接收後，送入AI模型中辨識手勢，再將辨識出來的手勢轉換為燈泡訊號，控制燈泡明暗。AI

## 二、專案架構

![image](https://github.com/user-attachments/assets/53c26561-00c3-4d1a-9dda-3fdcc1d6e216)

## 三、手勢設計

在這個專案中，將畫垂直線（螢幕朝右）設定為開燈，即燈泡亮度為100；將畫水平線（螢幕朝下）設定為關燈，即燈泡亮度為0；初始值為50。

## 四、預測模型

因為只需要分辨兩種手勢，所以不需要用太複雜的模型（避免導致過度擬合），因此我選擇使用SVM中kernel='linear' 的SVC，得到模型分辨兩種手勢的正確率為100%。

## 五、環境

python = 3.9.21

numpy              2.0.2

paho-mqtt          2.1.0

pandas             2.2.3

requests           2.32.3

scikit-learn       1.6.0

scipy              1.13.1

urllib3            2.3.0

wheel              0.44.0

## 六、報告(成功版本)
[google文件](https://docs.google.com/document/d/1-1_BiDmKK8tppAJLjib5xvtyZiqjc7SpORqcvTc5KGU/edit?usp=sharing)
[實作影片](https://drive.google.com/file/d/1x-uzpMYs7YXp1XTtHpyfDY7HKmoKWFYz/view?usp=sharing)

