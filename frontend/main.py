import streamlit as st
import requests 



st.header('Forum Predictor App')
st.image('eliza.png',width=100)
st.write('Type a question, and I can predict which forum that question is coming from')
st.write('Questions should come from these categories: `quantumcomputing`, `astronomy`, `martialarts`, `opendata`,`sports`, `ai`, `computergraphics`, `coffee`, `beer`')
question = st.text_input('Enter Text')
send = st.button('Predict Forum')
keys= {'question': question}


if send and (question.strip() == '' or len(question.strip()) < 10):
    st.warning('Please enter an actual question')


elif send and question != '':
    with st.spinner('Wait for it...'):
        prediction = requests.get("http://137.184.226.129/predict-forum", params=keys)
        prediction = prediction.json()
        st.write('Predicted Class: `{}`'.format(prediction['prediction']))
        st.write('Probability: `{}`'.format(prediction['Probability']))
        st.success('Done!')



