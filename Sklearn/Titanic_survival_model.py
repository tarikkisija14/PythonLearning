

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split



csvPath=r"C:\Users\tarik\Desktop\pocetnicki koraci\Sklearn\train.csv"

df=pd.read_csv(csvPath)

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})

X = df[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]]
y=df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def ModelTraining(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model


def EvaluateModel(model, X_test, y_test):
    y_pred=model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy:{acc:.4f}")



model=ModelTraining(X_train,y_train)
EvaluateModel(model,X_test,y_test)

joblib.dump(model,r"C:\Users\tarik\Desktop\pocetnicki koraci\Sklearn\Titanic.pkl")
