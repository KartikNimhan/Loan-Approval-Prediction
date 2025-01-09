import streamlit as st
import pandas as pd
from joblib import load
import logging
import sys
import joblib
import os

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

if os.path.exists("/.dockerenv"): 
    MODEL_PATH= '/app/models/loan_approval_model.pkl'
else:
    MODEL_PATH= 'D:/My projects/Loan Approval Prediction/model/loan_approval_model.pkl'


model = joblib.load(MODEL_PATH)


@st.cache_resource
def load_model():
    try:
        model = load(MODEL_PATH)
        logging.info("Model loaded successfully.")
        return model
    except Exception as e:
        logging.error(f"Error loading model: {str(e)}")
        st.error("Failed to load the model. Please check the file path and format.")
        sys.exit(1)


model = load_model()


st.title("Loan Approval Prediction")
st.write("This application predicts whether a loan will be approved based on the input details.")

st.header("Input Features")
no_of_dependents = st.selectbox("Number of Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["No", "Yes"])
income_annum = st.number_input("Annual Income", min_value=0, step=1000)
loan_amount = st.number_input("Loan Amount", min_value=0, step=1000)
loan_term = st.number_input("Loan Term (in months)", min_value=0, step=12)
cibil_score = st.number_input("CIBIL Score", min_value=300, max_value=900, step=1)
bank_asset_value = st.number_input("Bank Asset Value", min_value=0, step=1000)
total_assets = st.number_input("Total Assets", min_value=0, step=1000)


def preprocess_input(no_of_dependents, education, self_employed, income_annum,
                     loan_amount, loan_term, cibil_score, bank_asset_value, total_assets):
    try:
      
        education = 1 if education == "Graduate" else 0
        self_employed = 1 if self_employed == "Yes" else 0

        input_data = pd.DataFrame({
            "no_of_dependents": [int(no_of_dependents) if no_of_dependents != "3+" else 3],
            "education": [education],
            "self_employed": [self_employed],
            "income_annum": [income_annum],
            "loan_amount": [loan_amount],
            "loan_term": [loan_term],
            "cibil_score": [cibil_score],
            "bank_asset_value": [bank_asset_value],
            "total_assets": [total_assets]
        })

        return input_data
    except Exception as e:
        logging.error(f"Error in preprocessing input: {str(e)}")
        raise Exception("Input preprocessing failed.")


if st.button("Predict Loan Approval"):
    try:
        
        input_data = preprocess_input(no_of_dependents, education, self_employed, income_annum,
                                      loan_amount, loan_term, cibil_score, bank_asset_value, total_assets)


        input_array = input_data.drop(columns=['loan_status'], errors='ignore').to_numpy()

       
        model = load_model() 
        prediction = model.predict(input_array)
        result = "Approved" if prediction[0] == 1 else "Not Approved"
        st.success(f"The loan application is predicted to be: {result}")
    except Exception as e:
        logging.error(f"Prediction error: {str(e)}")
        st.error("An error occurred during prediction. Please try again.")
