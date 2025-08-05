import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib

csvPath=r"C:\Users\tarik\Desktop\pocetnicki koraci\Sklearn\EmailSVM.csv"


df=pd.read_csv(csvPath)

X=df[["contains_offer","contains_discount","length"]]
y=df["is_spam"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def TrainModel(X_train,y_train,kernel):
    model=SVC(kernel=kernel)
    model.fit(X_train,y_train)
    return model

def EvaluateModel(model,X_test,y_test):
    y_pred=model.predict(X_test)
    acc=accuracy_score(y_test,y_pred)
    print(f"Tacnost: {acc}")
    return acc


model=TrainModel(X_train,y_train,kernel="linear")
EvaluateModel(model,X_test,y_test)

joblib.dump(model,r"C:\Users\tarik\Desktop\pocetnicki koraci\Sklearn\ESVMTM.pkl")