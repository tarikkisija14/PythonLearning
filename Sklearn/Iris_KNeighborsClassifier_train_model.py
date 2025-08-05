from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib

def LoadIris():
    iris=load_iris()
    X=iris.data
    y=iris.target
    return X,y

def SplitIris(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def model_training(X_train,y_train,k):
    model=KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train,y_train)
    return model

def EvaluateModel(model,X_test,y_test):
    y_pred=model.predict(X_test)
    acc=accuracy_score(y_test,y_pred)
    print(f"Tacnost Modela:{acc:.2f}")

X,y=LoadIris()
X_train, X_test, y_train, y_test = SplitIris(X,y)
model = model_training(X_train,y_train,k=3)
EvaluateModel(model,X_test,y_test)

joblib.dump(model,r"C:\Users\tarik\Desktop\pocetnicki koraci\Sklearn\IKNCTM.pkl")

