import streamlit as st
import pandas as pd
import joblib

# Load model and encoder
model = joblib.load("trained_model.pkl")
encoder = joblib.load("encoder.pkl")

# Title
st.title("📊 Walmart Weekly Sales Prediction")
st.markdown("#### Enter details below and click 'predict' 🔮")

# Vertical inputs
store = st.selectbox("🏬 Select Store", [1, 2, 3, 4, 13, 20])
holiday = st.checkbox("🎉 Holiday Week? (Yes/No)")
temperature = st.slider("🌡️ Temperature (°F)", 20, 100, 60)
fuel_price = st.number_input("⛽ Fuel Price", value=3.5)
cpi = st.number_input("💰 CPI", value=200.0)
unemployment = st.number_input("📉 Unemployment Rate", value=8.0)
week = st.slider("📅 Week Number", 1, 52, 10)

# Predict button
if st.button("predict"):
    # Prepare input
    input_df = pd.DataFrame({
        "Store": [store],
        "Holiday_Flag": [1 if holiday else 0],
        "Temperature": [temperature],
        "Fuel_Price": [fuel_price],
        "CPI": [cpi],
        "Unemployment": [unemployment],
        "Week": [week]
    })

    # Transform and predict
    X_processed = encoder.transform(input_df)
    prediction = model.predict(X_processed)

    # Display results
    st.subheader("🔮 Predicted Weekly Sales")
    st.success(f"Estimated Sales: **${prediction[0]:,.2f}**")

    # Extra info
    st.markdown("### 📈 Factors Considered")
    st.write("Predictions are based on **store performance, holidays, CPI, unemployment, and weekly cycles.**")
