import streamlit as st
import requests 



st.header('Welcome to the Forum Predictor App built')
st.write('Type a question, and I can predict which forum that questions is coming from')
question = st.text_input('Enter Text')
send = st.button('Predict Forums')
keys= {'question': question}




if send:
    prediction = requests.get("http://137.184.226.129/predict-forum", params=keys)
    prediction = prediction.json()
    st.write(prediction)


