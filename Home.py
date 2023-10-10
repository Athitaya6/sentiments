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
st.image('./image/athitaya.jpg')

lot3="https://lottie.host/a0850c6f-4af2-4e46-9801-923b0d5f7e21/eBad93dNWe.json"
lottie3 = load_lottieurl(lot3)
st_lottie(lottie3)
st.balloons()