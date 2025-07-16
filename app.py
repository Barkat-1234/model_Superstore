# app.py

import streamlit as st
import pickle

# Load model
model = pickle.load(open('profit_model.pkl', 'rb'))

st.title("📈 Superstore profit prediction")

sales = st.number_input("Sales", value=100.0)
quantity = st.number_input("Quantity", value=1)
discount = st.number_input("Discount", value=0.0)

if st.button("Predict Profit"):
    input_data = [[sales, quantity, discount]]
    prediction = model.predict(input_data)
    st.success(f"Predicted Profit: ${prediction[0]:.2f}")
