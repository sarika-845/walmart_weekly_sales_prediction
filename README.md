
# Walmart Weekly Sales Prediction 📊

## 📌 Project Overview
This project predicts **weekly sales for Walmart stores** using multiple machine learning algorithms.  
The goal was to identify the best model for capturing complex, non‑linear relationships in the data and provide accurate forecasts.

---

## ⚙️ Data Preprocessing
- Split dataset into **Training (80%)** and **Testing (20%)**.
- Defined **numeric and categorical features** for scaling and encoding.
- Applied **StandardScaler** to normalize numeric columns.
- Used **OneHotEncoder** to convert categorical variables into numeric form.
- Combined transformations using **ColumnTransformer** and applied to training and test data.

---

## 🧪 Modeling Approach
- **Baseline Model** → Decision Tree Regressor for initial performance.
- **Multiple Algorithms Tested** → Linear Regression, Random Forest, KNN, and SVR.
- **Hyperparameter Tuning** → Optimized parameters to improve accuracy.
- **Evaluation Metrics** → R², RMSE, and MAE used consistently.

---

## 🏆 Best Model Selection
🌟 **Random Forest Regressor performed best**:
- **R² = 0.9475**
- **RMSE = 129,954**
- **MAE = 65,355**

It clearly outperformed Decision Tree, Linear Regression, and KNN, showing Random Forest captured complex, non‑linear relationships in the data effectively.

---

## 📂 Project Structure
walmart_weekly_sales_prediction/
│── app.py                # Streamlit app
│── model.pkl             # Trained Random Forest model
│── requirements.txt      # Dependencies
│── README.md             # Documentation
│── data/                 # Dataset folder

🌐 Deployment
This project can be deployed on Streamlit Cloud:
Connect GitHub repo
Auto‑install requirements
Launch app live
