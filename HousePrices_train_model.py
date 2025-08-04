import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score


csvPath=r"C:\Users\tarik\Desktop\pocetnicki koraci\HousePrices.csv"

def LoadData():
    try:
        df=pd.read_csv(csvPath)
        print(df.head())
        print(f"Ucitano: {len(df)}\n")
        print("Tipovi podataka:")
        print(df.dtypes)
        print("Broj null vrijednosti po kolonoma: ")
        print(df.isnull().sum())
        print("Statisticki pregled numerickih kolona: ")
        print(df.describe())
        return df
    except Exception as e:
        print(f"{e}")
        return None



def CleanData(df):
    for c in df.select_dtypes(include=[np.number]).columns:
        if df[c].isnull().sum() > 0:
            avg=df[c].mean()
            df[c].fillna(avg, inplace=True)
    df.to_csv(r"C:\Users\tarik\Desktop\pocetnicki koraci\HousePrices_Cleaned.csv", index=False)
    return df




def PrepareData(df):
    X=df[["Size(sqft)","Bedrooms","Bathrooms","Age(years)","DistanceToCityCenter(km)"]]
    y=df["Price(USD)"]
    return X,y



def SplitData(X,y):
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
    return X_train,X_test,y_train,y_test

def model_training(X_train,y_train):
    model=LinearRegression()
    model.fit(X_train,y_train)
    return model


def EvaluateModel(model,X_test,y_test):
    y_pred=model.predict(X_test)
    mse=mean_squared_error(y_test,y_pred)
    r2=r2_score(y_test,y_pred)

    print(f"Mean Squared Error (MSE): {mse:.2f}")
    print(f"R-squared (R2 Score): {r2:.2f}")

df = LoadData()
df = CleanData(df)
X, y = PrepareData(df)
X_train, X_test, y_train, y_test = SplitData(X, y)
model = model_training(X_train, y_train)
EvaluateModel(model, X_test, y_test)