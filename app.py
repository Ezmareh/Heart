import streamlit as st
import pickle
import numpy as np

# Load model

with open("heart_disease_model.pkl", "rb") as f:
model = pickle.load(f)

st.set_page_config(page_title="Heart Disease Predictor")

st.title("❤️ Heart Disease Prediction App")

st.write("Enter the values below and click Predict.")

# Find how many features the model expects

num_features = model.n_features_in_

st.info(f"This model expects {num_features} input features.")

# Create inputs automatically

inputs = []

for i in range(num_features):
value = st.number_input(
f"Feature {i + 1}",
value=0.0,
step=1.0
)
inputs.append(value)

# Predict

if st.button("Predict"):
try:
features = np.array([inputs])

```
    prediction = model.predict(features)

    st.success(f"Prediction: {prediction[0]}")

    if prediction[0] == 1:
        st.error("Heart Disease Detected")
    else:
        st.success("No Heart Disease Detected")

except Exception as e:
    st.error(f"Prediction error: {e}")
```
