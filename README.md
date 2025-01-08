# IoTtalk-final_project

一、手勢設計

在這個專案中，將畫垂直線（螢幕朝右）設定為開燈，即燈泡亮度為100；將畫水平線（螢幕朝下）設定為關燈，即燈泡亮度為0。

二、預測模型

因為只需要分辨兩種手勢，所以不需要用太複雜的模型（避免導致過度擬合），因此我選擇使用SVM中kernel='linear' 的SVC，得到模型分辨兩種手勢的正確率為100%。

三、環境

python = 3.9.21
numpy              2.0.2
paho-mqtt          2.1.0
pandas             2.2.3
requests           2.32.3
scikit-learn       1.6.0
scipy              1.13.1
urllib3            2.3.0
wheel              0.44.0

四、報告(成功版本)
https://docs.google.com/document/d/1-1_BiDmKK8tppAJLjib5xvtyZiqjc7SpORqcvTc5KGU/edit?usp=sharing

