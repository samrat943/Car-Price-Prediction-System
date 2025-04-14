import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

# Title
st.title("🚗 Car Price Prediction App")
st.write("Enter the details of the car to predict its selling price.")

# Sidebar for inputs
brand = st.selectbox("Brand", ["Maruti", "Hyundai", "Honda", "Toyota"])
year = st.slider("Year of Manufacture", 2000, 2024, 2015)
km_driven = st.number_input("Kilometers Driven", 0, 500000, 30000)
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG", "Electric"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.selectbox("Owner Type", ["First Owner", "Second Owner", "Third Owner", "Fourth & Above Owner", "Test Drive Car"])

# Predict Button
if st.button("Predict Price"):
    input_data = {
        "year": [year],
        "km_driven": [km_driven],
        "fuel_type": [fuel_type],
        "transmission": [transmission],
        "owner": [owner],
        "brand": [brand]
    }

    df = pd.DataFrame(input_data)
    df = pd.get_dummies(df)

    # Align input to match model columns
    model_features = joblib.load("model_features.pkl")  # Save model features from training
    for col in model_features:
        if col not in df.columns:
            df[col] = 0
    df = df[model_features]

    prediction = model.predict(df)[0]
    st.success(f"Estimated Selling Price: ₹ {round(prediction, 2)} Lakhs")
    