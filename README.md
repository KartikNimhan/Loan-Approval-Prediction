## **Loan Approval Prediction**

### **Overview**
This project is an end-to-end machine learning solution designed to predict loan approval based on applicant data. It covers all stages from data ingestion to model building and deployment. 

The application is built with **Streamlit** for the user interface, **MLflow** for experiment tracking, and deployed using **Docker**. CI/CD workflows are automated using **GitHub Actions**, and the Dockerized application is hosted on Docker Hub.

---

### **Features**
- **Data Ingestion**: Preprocessing raw data for analysis and training.
- **Model Building**: Train a machine learning model using scikit-learn.
- **Experiment Tracking**: Use MLflow to track experiments and log model metrics.
- **Deployment**: Serve the model with a Streamlit web application.
- **Containerization**: Use Docker for efficient deployment.
- **CI/CD**: Automate testing, building, and deployment workflows with GitHub Actions.

---

### **Variables Used**
The following variables are considered for loan approval prediction:

- **no_of_dependents**: Number of dependents the applicant has.
- **education**: Educational qualification of the applicant (Graduate/Non-Graduate).
- **self_employed**: Whether the applicant is self-employed (Yes/No).
- **income_annum**: Annual income of the applicant in monetary units.
- **loan_amount**: Loan amount requested by the applicant.
- **loan_term**: Duration of the loan term in months.
- **cibil_score**: Credit score of the applicant.
- **bank_asset_value**: Value of the applicant's assets with the bank.
- **loan_status**: Status indicating whether the loan is approved or rejected.
- **total_assets**: Total value of the applicant's assets, including bank and non-bank holdings.

---

### **Technologies Used**
- **Python**: Core programming language.
- **Streamlit**: Interactive web application.
- **MLflow**: Experiment tracking and model versioning.
- **Docker**: Application containerization.
- **GitHub Actions**: CI/CD pipeline automation.
- **scikit-learn**: Machine learning model training.
- **Pandas**: Data preprocessing and manipulation.

---
### ***Model working video:-**
https://github.com/user-attachments/assets/06b3b3c3-4d5c-4c17-bb66-4fc5d7c732ec

### **Getting Started**

#### **Clone the Repository**
```bash
git clone https://github.com/KartikNimhan/Loan-Approval-Prediction.git
cd Loan-Approval-Prediction
```

#### **Run Locally**
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the application:
   ```bash
   streamlit run app.py
   ```

#### **Run with Docker**
1. Build the Docker image:
   ```bash
   docker build -t loan-approval-app .
   ```
2. Run the application:
   ```bash
   docker run -p 8501:8501 loan-approval-app
   ```

#### **Docker Hub**
The prebuilt Docker image is available on Docker Hub. Pull and run it directly:
```bash
docker pull your-kartik8/loan-approval-predictor
docker run -p 8501:8501 kartik8/loan-approval-predictor
```

---

### **CI/CD with GitHub Actions**
The project is integrated with GitHub Actions to automate testing, building, and deployment workflows.

1. Push your changes to the GitHub repository.
2. GitHub Actions workflow will:
   - Test the code.
   - Build the Docker image.
   - Push the image to Docker Hub.

---

### **Code for Collaboration**
If you'd like to collaborate or work on this project, follow these steps:

1. **Fork the Repository**: 
   - Click on "Fork" at the top-right corner of this repository.
2. **Clone Your Fork**:
   ```bash
   git clone https://github.com/KartikNimhan/Loan-Approval-Prediction.git
   cd Loan-Approval-Prediction
   ```
3. **Create a New Branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make Changes and Commit**:
   ```bash
   git add .
   git commit -m "Add your commit message here"
   ```
5. **Push Changes**:
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Create a Pull Request**:
   - Go to the original repository.
   - Click "New Pull Request."

---

### **License**
This project is open-source and available under the [MIT License](LICENSE).

