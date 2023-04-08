import streamlit as st
import random

st.title("Random Number Generator")

# Define the range of the random number [MIN number, MAX number]
min_num = st.number_input("MIN number", value=0)
max_num = st.number_input("MAX number", value=100)

# Create a button to generate the random number
if st.button("Generate a Random Number"):
    random_num = random.randint(min_num, max_num)
    st.write(f"Random Number: {random_num}")


st.markdown('---')

st.markdown('[My Github Profile](https://github.com/CanGurcuoglu)')

