import streamlit as st
import random
import string

def generate_password(length,use_digits,use_special_characters):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits #Adds digits (0-9) if selected
    if use_special_characters:
        characters += string.punctuation #Adds special characters if selected 
    return ''.join(random.choice(characters) for _ in range(length)) 

st.title("Password Generator🔑")

length = st.slider("Select Password Length",min_value=8,max_value=32,value=12)
use_digits = st.checkbox("Include Digits ✅")
use_special_characters = st.checkbox("Include Special Characters ✅")
if st.button("Generate Password 🔘"):
     password = generate_password(length,use_digits,use_special_characters)
     st.success(f"Generated Password: {password}")

st.write("Developed by: Sohaib Touseef")
st.write("Build with ❤️ by [Sohaib Touseef](https://github.com/SohaibTouseef125)")


    