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

lot3="https://lottie.host/2e099151-4397-40ad-ae7b-249bbaf1e8df/gluEhZplO8.json"
lottie3 = load_lottieurl(lot3)
st_lottie(lottie3)
st.balloons()