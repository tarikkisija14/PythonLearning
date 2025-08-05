import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

csvPath=r"C:\Users\tarik\Desktop\pocetnicki koraci\Sklearn\College_Cleaned.csv"

df=pd.read_csv(csvPath)

df["Gender"]=df["Gender"].map({"F":0,"M":1})

X=df[["Age","Gender","MathScore","PhysicsScore","ChemistryScore","AttendanceRate","StudyHours","AverageGrade"]]
y=df["Passed"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def model_training(X_train,y_train,TreesCount):
    model=RandomForestClassifier(n_estimators=TreesCount,random_state=42)
    model.fit(X_train,y_train)
    return model

def EvaluateModel(model,X_test,y_test):
    y_pred=model.predict(X_test)
    acc=accuracy_score(y_test,y_pred)
    print(f"Tacnost modela: {acc:.2f}")

    features=X.columns
    impt=model.feature_importances_
    for i in range(len(features)):
        print(f"Feature {i}: {features[i]}")


model=model_training(X_train,y_train,100)
EvaluateModel(model,X_test,y_test)

