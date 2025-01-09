import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from src.Loan_Approval_Prediction.utils.exceptions import logging
from src.Loan_Approval_Prediction.utils.exceptions import CustomException
import sys

preprocessed_data_path = "D:/My projects/Loan Approval Prediction/data/preprocessed_data/processed_loan_data.csv"

def preprocess_data(raw_data_path):
    try:
        data = pd.read_csv(raw_data_path)

        data['total_assets'] = data['residential_assets_value'] + data['commercial_assets_value'] + data['luxury_assets_value']
        data = data.drop(columns=['residential_assets_value', 'commercial_assets_value', 'luxury_assets_value', 'loan_id'])

        label_encoders = {}
        for column in ['education', 'self_employed', 'loan_status']:
            le = LabelEncoder()
            data[column] = le.fit_transform(data[column])
            label_encoders[column] = le

        X = data.drop(['loan_status'], axis=1)
        y = data['loan_status']

        # Feature scaling
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Splitting the dataset into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

        # Saving the processed data
        data.to_csv(preprocessed_data_path, index=False)
        
        logging.info(f"Data preprocessed successfully and saved to {preprocessed_data_path}")
        return X_train, X_test, y_train, y_test

    except Exception as e:
        logging.error(f"An error occurred during data preprocessing: {str(e)}")
        raise CustomException(str(e), sys)

if __name__ == "__main__":
    raw_data_path = "D:/My projects/Loan Approval Prediction/data/raw_data/Load_Approval_Prediction.csv"
    preprocess_data(raw_data_path)
