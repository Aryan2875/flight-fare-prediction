
import streamlit as st
import joblib
import pandas as pd

model = joblib.load("models/flight_model.pkl")

st.title("✈️ Flight Fare Prediction System")

airline = st.selectbox("Airline", ["IndiGo", "Air India", "SpiceJet", "Vistara"])
source = st.selectbox("Source", ["Delhi", "Mumbai", "Kolkata", "Chennai"])
destination = st.selectbox("Destination", ["Cochin", "Delhi", "Hyderabad", "Bangalore"])
stops = st.selectbox("Total Stops", ["non-stop", "1 stop", "2 stops"])
day = st.slider("Journey Day", 1, 31)
month = st.slider("Journey Month", 1, 12)

if st.button("Predict Price"):
    input_df = pd.DataFrame({
        "Airline": [airline],
        "Source": [source],
        "Destination": [destination],
        "Total_Stops": [stops],
        "Journey_Day": [day],
        "Journey_Month": [month]
    })
    prediction = model.predict(input_df)
    st.success(f"Estimated Flight Price: ₹ {int(prediction[0])}")
