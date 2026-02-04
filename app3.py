import streamlit as st 

st.title("basic calculator app")

num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:")

operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiplication", "Division"])

if st.button("Calculate"):
    if operation == "Add":
        st.write(num1 + num2)
    elif operation == "Subtract":
        st.write(num1 - num2)
    elif operation == "Multiplication":
        st.write(num1 * num2)
    elif operation == "Division":
        st.write(num1 / num2)
        if num2 == 0:
            st.write("Cannot Divide By Zero")
        else:
            st.write("Answer:",num1/num2)
    elif operation == "Multiplication":
            st.write("Answer: ", num1*num2)
        
        
        