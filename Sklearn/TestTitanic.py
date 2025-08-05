from Titanic_survival_model import model,X_test,y_test


y_pred = model.predict(X_test)


for i in range(len(X_test)):
    stvarni = y_test.iloc[i]
    predikcija = y_pred[i]
    status_pred = "PREZIVIO" if predikcija == 1 else "NIJE PREŽIVIO"
    status_stvarni = "PREZIVIO" if stvarni == 1 else "NIJE PREŽIVIO"
    print(f"Putnik {i + 1}: AI Predikcija: = {status_pred} | Stvarni ishod = {status_stvarni}")
