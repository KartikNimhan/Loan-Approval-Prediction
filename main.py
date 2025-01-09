import os
from src.Loan_Approval_Prediction.utils.exceptions import logging
from src.Loan_Approval_Prediction.utils.exceptions import CustomException
from src.Loan_Approval_Prediction.data_ingestion import download_data
from src.Loan_Approval_Prediction.data_preprocessing import preprocess_data
from src.Loan_Approval_Prediction.model_trainer import train_model
import sys

def main():
    try:
        # Define paths
        raw_data_path = "D:/My projects/Loan Approval Prediction/data/raw_data/Load_Approval_Prediction.csv"
        processed_data_path = "D:/My projects/Loan Approval Prediction/data/preprocessed_data/processed_loan_data.csv"
        model_path = "D:/My projects/Loan Approval Prediction/model/loan_approval_model.pkl"

        # Step 1: Data Ingestion
        logging.info("Starting data ingestion...")
        download_data()
        logging.info("Data ingestion completed.")

        # Step 2: Data Preprocessing
        logging.info("Starting data preprocessing...")
        X_train, X_test, y_train, y_test = preprocess_data(raw_data_path)
        logging.info(f"Data preprocessing completed. Processed data saved at {processed_data_path}.")

        # Step 3: Model Training
        logging.info("Starting model training...")
        train_model(X_train, y_train, X_test, y_test)
        logging.info(f"Model training completed. Model saved at {model_path}.")

        logging.info("Pipeline execution completed successfully.")

    except CustomException as e:
        logging.error(f"Pipeline failed with error: {str(e)}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        raise CustomException(str(e), sys)

if __name__ == "__main__":
    main()
