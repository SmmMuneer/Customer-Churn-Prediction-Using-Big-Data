# Customer-Churn-Prediction-Using-Big-Data
Customer Churn Prediction in the Telecommunication Sector Using Machine Learning This project focuses on building a machine learning-based predictive system to accurately identify telecom customers likely to churn (leave the service). Using a cleaned and preprocessed dataset of over 64,000 customer records from the telecommunications sector. 

## ✅ Objective
- To build machine learning models that accurately predict customer churn.
- To compare multiple classification algorithms and select the most effective.
- To identify the most influential features that lead to churn.
- To deploy a Flask-based web application for real-time churn prediction.

## 🧠 Models Used
- Logistic Regression  
- Decision Tree  
- Random Forest  
- XGBoost (Best performer)

## 🎯 Key Results

| Model              | Accuracy | Precision | Recall | F1 Score |
|-------------------|----------|-----------|--------|----------|
| Logistic Regression | 81.72%   | 79.67%    | 82.31% | 80.97%   |
| Decision Tree       | 96.44%   | 96.30%    | 96.36% | 96.33%   |
| Random Forest       | 96.57%   | 95.57%    | 97.20% | 96.38%   |
| **XGBoost**         | **96.82%** | **96.03%** | **97.27%** | **96.65%** |

✅ Based on performance metrics, **XGBoost** was selected for deployment.
## 🔍 Feature Importance (XGBoost)

Top predictors of churn:
- **Payment Delay**
- **Gender**
- **Support Calls**
- **Usage Frequency**
- Contract Length
- Tenure

## 🧪 Hypothesis Testing
A t-test was conducted between **Tenure** and **Churn**, and the results indicated a statistically significant difference. This supports the hypothesis that customers with lower tenure are more likely to churn.

## 🌐 Web Application (Flask)

An interactive web interface was developed using Flask. The app allows users to input customer data and instantly receive churn predictions. Based on the result, users are redirected to either:

- `churn.html`: Customer is at high risk of churn  
- `not_churn.html`: Customer is likely to stay
- index.html

Features include dropdowns for categorical fields like gender, subscription type, and contract length, making the interface user-friendly.
