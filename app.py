import streamlit as st
import requests
from streamlit_lottie import st_lottie
from DHHACKATHON import evaluvate

def load_lottieurl(url):
    r = requests.get(url)
    return r.json()

st.set_page_config(page_title="DeerHacks 2023", layout = "wide")
with st.container():
    animation = load_lottieurl("https://lottie.host/03f740df-28ea-4fe5-a6e4-84766147ca7f/qOivh54jez.json")
    st_lottie(animation, height = "200px")

with st.container():
    with st.form(key = "Run"):
        st.header("Welcome to WebsiteRater")
        st.write("A project designed to rate and recommend features to improve for a given website")
        user_input_text = st.text_input("Enter the website here: ")
        submit = st.form_submit_button("Evaluvate")
    if submit:
        result = evaluvate(user_input_text)
        for i in result:
            st.write(i)
