import json
import time
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
st.header("การวิเคราะห์ความรู้สึกภาษาไทย")
st.header("Athitaya Kakandee")

lot3="https://lottie.host/57654ef5-32e3-448d-b5f6-ed845b245c93/nsc1xfV677.json"
lottie3 = load_lottieurl(lot3)
#st_lottie(lottie3)

col1, col2 = st.columns(2)
with col1:
    st_lottie(lottie3)
with col2:
    st.image('./image/athitaya.jpg')
st.balloons()