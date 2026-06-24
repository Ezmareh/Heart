import streamlit as st
import pickle
import numpy as np

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("My ML Model")

st.write("Enter feature values below:")

# Example: 4 input features
feature1 = st.number_input("Feature 1")
feature2 = st.number_input("Feature 2")
feature3 = st.number_input("Feature 3")
feature4 = st.number_input("Feature 4")

if st.button("Predict"):
    features = np.array([[feature1, feature2, feature3, feature4]])
    prediction = model.predict(features)

    st.success(f"Prediction: {prediction[0]}")
