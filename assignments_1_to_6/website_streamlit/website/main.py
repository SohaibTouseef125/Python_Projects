import streamlit as st

st.set_page_config(page_title="My first website",page_icon="🌏",layout="centered")
st.title("🌏 Welcome to my first website🌏")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

if page == "Home":
    st.header("Home")
    st.write("This is the home page")
    name = st.text_input("Enter your name")
    if name:
        st.success(f"Hello {name} Thanks for visiting")
elif page == "About":
    st.header("About")
    st.write("This is the about page")
   
    
else:
    st.header("Contact")
    st.write("This is the contact page")
    email = st.text_input("Enter your email")
    meassage = st.text_area("Enter your message")
    if st.button("Send"):
        st.success("Thank you for your message")
