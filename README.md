## **Loan Approval Prediction Model**
A machine learning model that predicts whether a loan application should be approved based on applicant details.

## Project Overview
This project builds a Machine Learning model to predict loan approval based on applicant attributes such as incone, credit history, loan amount, and employment status. The goal is to help financial institutions automate the loan approval process.

## Dataset
The dataset used in this project is sourced from Kaggle:

Loan Prediction Problem Dataset: https://www.kaggle.com/datasets/altruistdelhite04/loan-prediction-problem-dataset

Credits to the original dataset authors on Kaggle.

Features:
- Gender
- Married
- Dependents
- Education
- Self_Employed
- ApplicantIncome
- CoapplicantIncome
- LoanAmount
- Loan_Amount_Term
- Credit_History
- Property_Area

Target Variable:
- Loan_Status (Approved / Rejected)

## Project Overflow
1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Model training
6. Model evaluation
7. Prediction

## Data Preprocessing
- Handling missing values
- Encoding categorical variables
- Feature Scaling
- Train-test split

## Models Used
- Logistic Regression
- Decision Tree
- Random Forest

Logistic Regression gave the best performance with 83.73% accuracy

## Model Evaluation
- Best Model: Logistic Regression
- Accuracy: 83.73%
- Macro F1 Score: 0.77
- Precision: 0.81
- Recall: 1 (for approved loans)
- Confusion Matrix:
 
  [[18 20]
  
   [0  85]]

## Loan Approval Prediction API

This project builds a machine learning model to predict loan approval 
based on applicant financial and demographic features.

The trained model is served using a REST API built with FastAPI.

### API Endpoint
POST /predict

### Example Response
{
  "prediction": 1
}

### API Documentation Interface
## Loan Approval Prediction API

This project builds a machine learning model to predict loan approval 
based on applicant financial and demographic features.

The trained model is served using a REST API built with FastAPI.

### API Endpoint
POST /predict

### Example Response
{
  "prediction": 1
}

### API Documentation Interface
<img width="2183" height="1955" alt="image" src="https://github.com/user-attachments/assets/97680f01-f903-4dbd-bf70-b09cd6033619" />






## Author
Author: Pragya S

Github: https://github.com/pragyas0207
