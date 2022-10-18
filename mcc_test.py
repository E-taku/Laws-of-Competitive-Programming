import numpy as np
import pandas as pd

#混同行列の各要素
N_TP = 1000
N_FP = 200
N_FN = 100
N_TN = 5000

#混同行列を生成して出力
conf_MX = pd.DataFrame({"Positive":[N_TP,N_FN], "Negative":[N_FP,N_TN]}, 
                        index=["Positive","Negative"])
print(conf_MX)

TP = [[1,1] for i in range(N_TP)] #[1,1]のデータをTrue Positiveの数だけ作成
FP = [[1,0] for i in range(N_FP)] #[1,0]のデータをFalse Positiveの数だけ作成
FN = [[0,1] for i in range(N_FN)] #以下同様に作成
TN = [[0,0] for i in range(N_TN)]

#予測{0,1}、正解{0,1}をカラムに持ったデータフレームを作成して出力
df = pd.DataFrame(TP + FP + FN + TN, columns=["pred", "truth"])
print(df.head(10))

mcc = (N_TP*N_TN - N_FP*N_FN) / np.sqrt((N_TP+N_FP)*(N_FN+N_TN)*(N_TP+N_FN)*(N_FP+N_TN))
corr = df.corr()

print("マシューズ相関係数:" + str(mcc))
print("ピアソン相関係数　:" + str(corr["pred"]["truth"]))
