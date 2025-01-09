import mlflow
import mlflow.sklearn
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, log_loss
from src.Loan_Approval_Prediction.utils.exceptions import logging
from src.Loan_Approval_Prediction.utils.exceptions import CustomException
import sys
import joblib


mlflow.set_experiment('Loan_Approval_Prediction')

def train_model(X_train, y_train, X_test, y_test):
    try:
        with mlflow.start_run():  
            model = LogisticRegression()
            model.fit(X_train, y_train)

            mlflow.log_param('model_type', 'LogisticRegression')

            y_pred = model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            logloss = log_loss(y_test, model.predict_proba(X_test))

            mlflow.log_metric('accuracy', accuracy)
            mlflow.log_metric('log_loss', logloss)

            mlflow.sklearn.log_model(model, 'Loan_Approval_Prediction')

            logging.info(f"Model trained: Accuracy = {accuracy}, Log Loss = {logloss}")

            joblib.dump(model, 'D:/My projects/Loan Approval Prediction/model/loan_approval_model.pkl')

    except Exception as e:
        logging.error(f"An error occurred during model training: {str(e)}")
        raise CustomException(str(e), sys)

if __name__ == "__main__":
    from data_preprocessing import preprocess_data
    
    X_train, X_test, y_train, y_test = preprocess_data("D:/My projects/Loan Approval Prediction/data/raw_data/Load_Approval_Prediction.csv")
    train_model(X_train, y_train, X_test, y_test)
