import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score

csvPath=r"C:\Users\tarik\Desktop\pocetnicki koraci\Sklearn\College.csv"

def LoadData():
    try:
        df = pd.read_csv(csvPath)
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

df=LoadData()

def CleanData(df):
    for c in df.select_dtypes(include=[np.number]).columns:
        if df[c].isnull().sum() > 0:
            avg = df[c].mean()
            df[c].fillna(avg, inplace=True)

    if "AttendanceRate" in df.columns:
        min = df["AttendanceRate"].min()
        max = df["AttendanceRate"].max()
        df["AttendanceRate"] = (df["AttendanceRate"] - min) / (max - min)



    df["AverageGrade"] = df[["MathScore", "PhysicsScore", "ChemistryScore"]].mean(axis=1)
    df["PassedText"] = df["Passed"].apply(lambda x: "YES" if x == 1 else "NO")

    print("Ocisceni podaci:\n")
    print(df.head(10))
    df.to_csv(r"C:\Users\tarik\Desktop\pocetnicki koraci\Sklearn\College_Cleaned.csv", index=False)
    return df

dfCleaned=CleanData(df)

X=dfCleaned[["AttendanceRate", "StudyHours","AverageGrade"]]
y=dfCleaned["Passed"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model=LogisticRegression()
model.fit(X_train, y_train)

y_pred=model.predict(X_test)

acc=accuracy_score(y_test, y_pred)

print(f"Tacnost modela: {acc:.2f}")
