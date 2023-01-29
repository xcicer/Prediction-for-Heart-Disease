import streamlit as st
import pickle
import pandas as pd
import numpy as np
pickled_model = pickle.load(open('model.pkl', 'rb'))
st.title("prediction for Heart Diseas")
age = st.text_input("Input age") 
sex = st.text_input("Input sex, 1 = male, 0 = female", 0,1) 
cp = st.slider("Choose type for chest pain",0,4)
trestbps = st.text_input("input resting blood pressure (in mm Hg on admission to the  hospital")
chol = st.text_input("input serum cholestoral in mg/dl")
fbs = st.text_input("(fasting blood sugar > 120 mg/dl)  1 = true, 0 = false")
restecg = st.text_input("restecg: resting electrocardiographic results, 0 = Normal, 1 = having ST-T wave abnormality, 2 = showing probable or definite left ventricular hypertrophy by Estes' criteria")
thalach = st.text_input("thalach: maximum heart rate achieved")
exang = st.text_input("exercise induced angina (1 = yes; 0 = no)")
oldpeak = st.text_input("ST depression induced by exercise relative to rest")
slope = st.text_input("the slope of the peak exercise ST segment, Value 1: upsloping, Value 2: flat, Value 3: downsloping")
ca = st.slider("number of major vessels (0-3) colored by flourosopy", 0,3)
thal = st.slider("3 = normal; 6 = fixed defect; 7 = reversable defect", 0,10)
prediction = st.button('Predict')
if prediction:
    X = np.array([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
    y = pd.DataFrame([X])
    prediction = pickled_model.predict(y)
    if prediction[0] == 1: 
         st.subheader('Paitent has heart disease')
    else: 
        st.subheader("Paitent does not have Cancer") 



#thal: 3 = normal; 6 = fixed defect; 7 = reversable defect


    

# ca: number of major vessels (0-3) colored by flourosopy