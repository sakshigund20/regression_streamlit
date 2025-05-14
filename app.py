import streamlit as st
import joblib
import numpy as np

model=joblib.load('regression_model.joblib')

st.title("Job Package Prediction Based on CGPA")
st.write("Enter your CGPA to predict the expected job package:")

cgpa=st.number_input("CGA",min_value=0.0,max_value=10.0,step=0.1)

if st.button("Predict Package"):
    input_data=np.array([[cgpa]])
    prediction=model.predict(input_data)
    predicted_value=float(prediction[0])
    st.success(f"Predicted Package:₹{predicted_value:,.2f}LPA")