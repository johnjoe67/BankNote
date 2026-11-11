# Banknote Authentication (Machine Learning)

A Python desktop app that predicts whether a banknote is **real or forged** using a Decision Tree classifier trained on the UCI Banknote Authentication dataset.

## Features
- Train a scikit-learn `DecisionTreeClassifier` with a selectable random seed
- Test the model and view the confusion matrix and accuracy
- Enter variance, skewness, curtosis and entropy to predict a new banknote
- Real/forged image feedback and a prediction history table
- Feature importance chart (matplotlib)

## Tech
Python · Tkinter · scikit-learn · pandas · matplotlib

## How to run
```
pip install -r requirements.txt
python ML.py
```
Run from inside the project folder so the CSV and images are found.

## Dataset
`data_banknote_authentication.csv` — features extracted from images of genuine and forged banknotes (UCI Machine Learning Repository).
