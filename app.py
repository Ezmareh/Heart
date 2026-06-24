import streamlit as st
import pickle

st.title("Model Debugger")

with open("heart_disease_model.pkl", "rb") as f:
model = pickle.load(f)

st.success("Model loaded successfully")

st.write("Model type:", type(model))

if hasattr(model, "n_features_in_"):
st.write("Expected number of features:", model.n_features_in_)
else:
st.write("Model does not expose n_features_in_")
