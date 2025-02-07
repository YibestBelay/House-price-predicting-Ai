import streamlit as st
import requests

# Title and Description
st.title("🏡 House Price Prediction App")
st.write("Enter the house features below to predict the price.")

# Input Form
with st.form("prediction_form"):
    rm = st.number_input("Average number of rooms (RM):", min_value=1.0, max_value=10.0, step=0.1)
    lstat = st.number_input("Percentage lower status of the population (LSTAT):", min_value=0.0, max_value=40.0, step=0.1)
    ptratio = st.number_input("Pupil-teacher ratio (PTRATIO):", min_value=10.0, max_value=30.0, step=0.1)
    indus = st.number_input("Proportion of non-retail business acres per town (INDUS):", min_value=0.0, max_value=30.0, step=0.1)
    
    # Submit Button
    submit_button = st.form_submit_button(label="Predict Price")

# Prediction Logic
if submit_button:
    # Backend API URL (update with your Render-deployed FastAPI URL)
    api_url = "http://127.0.0.1:8000/predict/"

    # Prepare input data
    input_data = {
        "rm": rm,
        "lstat": lstat,
        "ptratio": ptratio,
        "indus": indus
    }
    
    try:
        # Send request to the API
        response = requests.post(api_url, json=input_data)
        
        if response.status_code == 200:
            prediction = response.json()
            predicted_price = prediction.get("predicted_price", "N/A")
            st.success(f"The predicted house price is: ${predicted_price}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
