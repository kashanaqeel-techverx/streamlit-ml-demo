import streamlit as st
import pandas as pd
import numpy as np
import pickle

# --- Page setup ---
st.set_page_config(page_title="Iris Classifier Demo 🌸", page_icon="🌸")

st.title("Iris Flower Classification 🌼")
st.write("A simple demo ML app deployed on Cloud Run using Streamlit.")

# --- Load pre-trained model ---
with open("model/iris_model.pkl", "rb") as f:
    model = pickle.load(f)

# --- Sidebar inputs ---
st.sidebar.header("Input Features")
sepal_length = st.sidebar.slider("Sepal length (cm)", 4.0, 8.0, 5.0)
sepal_width = st.sidebar.slider("Sepal width (cm)", 2.0, 4.5, 3.0)
petal_length = st.sidebar.slider("Petal length (cm)", 1.0, 7.0, 4.0)
petal_width = st.sidebar.slider("Petal width (cm)", 0.1, 2.5, 1.2)

# --- Prediction ---
if st.button("Predict"):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)[0]
    st.success(f"Predicted Species: **{prediction}** 🌺")
