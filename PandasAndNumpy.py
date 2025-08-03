import pandas as pd
import tkinter as tk
import os
import numpy as np

csvPath=r"C:\Users\tarik\Desktop\pocetnicki koraci\College.csv"


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



def CleanData(df):


        for c in df.select_dtypes(include=[np.number]).columns:
            if df[c].isnull().sum() > 0:
                avg=df[c].mean()
                df[c].fillna(avg, inplace=True)

        if "AttendanceRate" in df.columns:
            min=df["AttendanceRate"].min()
            max=df["AttendanceRate"].max()

            df["AttendanceRate"]=(df["AttendanceRate"]-min)/(max-min)

        df["AverageGrade"] = df[["MathScore", "PhysicsScore", "ChemistryScore"]].mean(axis=1)
        df["PassedText"]=df["Passed"].apply(lambda x: "YES" if x==1 else "NO")

        print("Ocisceni podaci:\n")
        print(df.head(10))
        return df


def AnalyzeData(df):

    if df is None:
        print("Nema podataka za analizu")
        return

    if "AverageGrade" not in df.columns:
        print("Podaci nisu oceisceni,nema te kolone")
        return

    data=df[["StudyHours","AverageGrade"]].to_numpy()

    study_hours=data[:,0]
    average_grade=data[:,1]

    mean_study=np.mean(study_hours)
    mean_grade=np.mean(average_grade)

    std_study=np.std(study_hours)
    std_grade=np.std(average_grade)

    correl=np.corrcoef(study_hours,average_grade)[0,1]

    print(f"Prosjecno vrijeme ucenja: {mean_study:.2f}")
    print(f"Prosjecna ocjena: {mean_grade:.2f}")
    print(f"Standardna devijacija sati ucenja: {std_study:.2f}")
    print(f"Standardna devijacija prosjecnih ocjena {std_grade:.2f}")
    print(f"Korelacija između sati učenja i prosječne ocjene: {correl:.2f}")

df=LoadData()
df=CleanData(df)
AnalyzeData(df)