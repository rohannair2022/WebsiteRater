import streamlit as st
import requests
from streamlit_lottie import st_lottie
from DHHACKATHON import evaluvate, calculate_contrast_ratio

def load_lottieurl(url):
    r = requests.get(url)
    return r.json()

def rgb_picker1():
    # Slider for Red component
    red = st.slider("Red", 0, 255, 0, key="red_slider")
    # Slider for Green component
    green = st.slider("Green", 0, 255, 0, key="green_slider")
    # Slider for Blue component
    blue = st.slider("Blue", 0, 255, 0, key="blue_slider")
    # Display the selected color
    selected_color = (red, green, blue)
    # Display the color preview
    color_preview = f'<div style="width:50px; height:50px; background-color:rgb({red},{green},{blue});"></div>'
    st.markdown(color_preview, unsafe_allow_html=True)
    return selected_color

def rgb_picker2():
    # Slider for Red component
    red = st.slider("Red", 0, 255, 0)
    # Slider for Green component
    green = st.slider("Green", 0, 255, 0)
    # Slider for Blue component
    blue = st.slider("Blue", 0, 255, 0)
    # Display the selected color
    selected_color = (red, green, blue)
    # Display the color preview
    color_preview = f'<div style="width:50px; height:50px; background-color:rgb({red},{green},{blue});"></div>'
    st.markdown(color_preview, unsafe_allow_html=True)
    return selected_color

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

with st.container():
    left1, left2, middle1, middle2, right1, right2 = st.columns(6)
    if submit:
        lst = evaluvate(user_input_text)
        with left1:
            animation = load_lottieurl("https://lottie.host/85efa1de-8662-4790-9191-4d2d453e2710/IECaGx3IVa.json")
            st_lottie(animation, height = "100px")
            st.write("Your header score is: ", lst[0][0])
            st.write(lst[0][1])
        with left2:
            animation = load_lottieurl("https://lottie.host/85efa1de-8662-4790-9191-4d2d453e2710/IECaGx3IVa.json")
            st_lottie(animation, height = "100px")
            st.write("Your body score is: ", lst[1][0])
            st.write(lst[1][1])
        with middle1:
            animation = load_lottieurl("https://lottie.host/85efa1de-8662-4790-9191-4d2d453e2710/IECaGx3IVa.json")
            st_lottie(animation, height = "100px")
            st.write("Your footer score is: ", lst[2][0])
            st.write(lst[2][1])
        with middle2:
            animation = load_lottieurl("https://lottie.host/5d9f98f3-6023-4aba-a108-bc26c6789c58/9BjFYwHJL4.json")
            st_lottie(animation, height = "100px")
            st.write("Your alt score is: ", lst[3][0])
            st.write(lst[3][1])
        with right1:
            animation = load_lottieurl("https://lottie.host/32b31717-8c71-4b41-9c1a-6c83e9910c69/VBqJvDgJvA.json")
            st_lottie(animation, height = "100px")
            st.write("Your loading score is: ", lst[4][0])
            st.write(lst[4][1])
        with right2:
            animation = load_lottieurl("https://lottie.host/23aca1f4-d603-49e6-9772-0364d78b2ee3/r9uuwSE0kL.json")
            st_lottie(animation, height = "100px")
            st.write("Your responsive score is: ", lst[5][0])
            st.write(lst[5][1])

    st.subheader("Test a font text and background contrast to see if its a good fit")
    value1 = rgb_picker1()
    value2 = rgb_picker2()
    with st.form(key="Rgb"):

        submit = st.form_submit_button("Evaluate")

        if submit:
            st.write(calculate_contrast_ratio(value1, value2)[0])


