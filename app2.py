import streamlit as st 

st.title("my age and city app")

age = st.slider("enter your age" , 1 , 100)
city = st.selectbox("select your city" , ["MUMBAI" , "DELHI" , "CHENNAI" , "KERELA"])

if st.button("Your details:"):
    st.write("Your age is:", age)
    st.write("You live in:", city)