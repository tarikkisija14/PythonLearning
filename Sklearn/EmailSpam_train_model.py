import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report,accuracy_score

csvPath=r"C:\Users\tarik\Desktop\pocetnicki koraci\Sklearn\EmailSpam.csv"

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
    df.dropna(inplace=True)
    df['email']=df['email'].astype(str)
    return df



def PrepareData(df):
    vectorizer = CountVectorizer()
    X=vectorizer.fit_transform(df['email'])
    y=df['oznaka']
    return X, y, vectorizer


def SplitData(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def TrainModel(X_train,  y_train):
    model = MultinomialNB()
    model.fit(X_train, y_train)
    return model

def EvaluateModel(model, X_test, y_test):
    y_pred = model.predict(X_test)
    acc=accuracy_score(y_test, y_pred)
    print(f"Tacnost: {acc:.2f}")
    print("Detaljan izvjestaj:")
    print(classification_report(y_test, y_pred))

df=LoadData()
df=CleanData(df)
X,y,vectorizer=PrepareData(df)
X_train, X_test, y_train, y_test = SplitData(X, y)
model = TrainModel(X_train, y_train)
EvaluateModel(model, X_test, y_test)