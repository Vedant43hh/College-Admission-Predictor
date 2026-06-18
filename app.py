import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Dataset load
df = pd.read_csv("admission_predict.csv")

# Features aur target
X = df.drop(["Chance of Admit "], axis=1)
if "Serial No." in X.columns:
    X = X.drop(["Serial No."], axis=1)

y = df["Chance of Admit "]

# Model train
model = LinearRegression()
model.fit(X, y)

st.title("🎓 College Admission Predictor")

gre = st.number_input("GRE Score", 290, 340, 320)
toefl = st.number_input("TOEFL Score", 90, 120, 110)
univ = st.slider("University Rating", 1, 5, 3)
sop = st.slider("SOP", 1.0, 5.0, 3.0, 0.5)
lor = st.slider("LOR", 1.0, 5.0, 3.0, 0.5)
cgpa = st.number_input("CGPA", 0.0, 10.0, 8.5)
research = st.selectbox("Research Experience", [0, 1])

if st.button("Predict Admission Chance"):
    data = np.array([[gre, toefl, univ, sop, lor, cgpa, research]])
    prediction = model.predict(data)[0]

    st.success(f"Chance of Admission: {prediction*100:.2f}%")