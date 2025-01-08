from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

# 讀入檔案
data=pd.read_csv("combine2.csv")

inputs=data.drop('label',axis='columns') #inputs放需要訓練的欄位
target=data['label'] #target放label
# print(target.head())

#拆分訓練集與測試集
X=inputs
y=target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
# model=DecisionTreeClassifier().fit(X_train,y_train)
# 用建立好的模型來預測資料
# model.predict(X_test)
# 檢驗模型的正確率
# model.score(X_test,y_test)

#沒拆
#X=inputs
#y=target


"使用自己選擇的模型"
#model = DecisionTreeClassifier().fit(X,y)
# model = RandomForestClassifier(n_estimators=20).fit(X,y)
model=svm.SVC(kernel='linear', C=1)
model.fit(X_train,y_train)

"通常會用測試集看分數"
print(f'model score={model.score(X_test,y_test)*100}%')
predicted=model.predict(X_test)
df = pd.crosstab(y_test, predicted.astype(int), normalize='index',
                 rownames=['label'], colnames=['predict']).round(4).apply(lambda r: r*100)
print("%s\n" % df)
#匯出模型
import pickle

# model_filename='random_forest_model.pkl'
model_filename='svm_rbf_model.pkl'
with open(model_filename,'wb')as file: 
    pickle.dump(model,file)
print("模型已訓練完畢")