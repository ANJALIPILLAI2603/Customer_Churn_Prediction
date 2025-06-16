# Customer Churn Prediction Using ANN and Random Forest

This project focuses on predicting whether a customer will churn (leave the bank) using historical data and machine learning techniques. It includes a deep learning model built with TensorFlow/Keras and a comparative Random Forest model, accompanied by data exploration and evaluation metrics.

---

## 📂 Dataset Overview

- **Source:** `Churn_Modelling.csv`
- **Records:** 10,000 customers
- **Features:** Customer demographics, banking activity, account balance, product usage, etc.
- **Target Variable:** `Exited` (1 = Churned, 0 = Stayed)

---

## 🛠️ Tools & Technologies

- **Languages:** Python
- **Libraries:** TensorFlow, Keras, Scikit-learn, Pandas, Seaborn, Matplotlib
- **Models:** ANN (2 hidden layers), Random Forest

---

## 🔍 Exploratory Data Analysis (EDA)

Performed visual analysis on key features:
- Churn distribution
- Age vs Churn
- Geography vs Churn
- Feature correlation heatmap

These insights guided model feature selection and understanding of business impact.

---

## 🧠 Model 1: Artificial Neural Network (ANN)

- **Framework:** TensorFlow / Keras
- **Architecture:** 2 hidden layers with ReLU activation
- **Output Layer:** Sigmoid activation (binary classification)
- **Loss Function:** Binary Crossentropy
- **Optimizer:** Adam
- **Accuracy:** 85.8%
- **AUC Score:** 0.86

---

## 🌲 Model 2: Random Forest (Comparison)

- **Library:** Scikit-learn
- **Configuration:** 100 estimators
- **Accuracy:** 86.6 %
- **AUC Score:** 0.8662

---

## 📈 Evaluation Metrics

- Confusion Matrix
- Classification Report (Precision, Recall, F1-score)
- ROC Curve & AUC Score
- Side-by-side model comparison for business decision support

---

## 🧪 Single Customer Prediction

Used both ANN and Random Forest to predict churn on a sample customer with the following features:

- Geography: France  
- Credit Score: 600  
- Gender: Male  
- Age: 40  
- Balance: \$60,000  
- Products: 2  
- Credit Card: Yes  
- Active Member: Yes  
- Estimated Salary: \$50,000  

✅ The ANN predicted the customer would **stay**.  
🔄 Prediction matched Random Forest’s output in this case.

---

## 🚀 Future Enhancements

- Deploy model via **Streamlit** for interactive UI  
- Add **XGBoost** for improved performance benchmarking  
- Optimize hyperparameters using **GridSearchCV / Keras Tuner**  
- Convert into a mini decision-support system for bank analysts

---

## 🧾 Author

**Anjali Pillai**  
Aspiring Data Scientist | AI & Data Science Engineer  
[LinkedIn Profile](www.linkedin.com/in/anjali-pillai-367b2b259) 

---

