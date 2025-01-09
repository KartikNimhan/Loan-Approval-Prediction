import os
import requests
from src.Loan_Approval_Prediction.utils.exceptions import logging
from src.Loan_Approval_Prediction.utils.exceptions import CustomException
import sys

raw_data_path = os.path.join("D:/My projects/Loan Approval Prediction/data/raw_data", "Load_Approval_Prediction.csv")

def download_data():
    try:
        file_id = '1evRFGf9fEhKI8uR_kwWaqhMHk04HaMh4' 
        url = f"https://drive.google.com/uc?id={file_id}"
        response = requests.get(url)

        if response.status_code == 200:
            os.makedirs(os.path.dirname(raw_data_path), exist_ok=True)
            with open(raw_data_path, 'wb') as f:
                f.write(response.content)
            logging.info(f"Data downloaded successfully to {raw_data_path}")
        else:
            logging.error(f"Failed to download data. Status code: {response.status_code}")
    except Exception as e:
        logging.error(f"An error occurred while downloading data: {str(e)}")
        raise CustomException(str(e), sys)

if __name__ == "__main__":
    download_data()
