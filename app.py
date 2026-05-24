import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

st.title("Bank APK Fraud Detection")

feature1 = st.number_input("Feature 1")
feature2 = st.number_input("Feature 2")
feature3 = st.number_input("Feature 3")

if st.button("Predict"):

    data = np.array([[feature1, feature2, feature3]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Fraud APK")
    else:
        st.success("Safe APK")