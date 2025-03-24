import numpy as np
import streamlit as st
st.set_page_config(page_title="Numpy Log Calculator")
st.title("Numpy Calculator")

with st.form("input_form"):
    choice = st.selectbox("Select option", ["Convert number to log form", "Convert log form to number"])
    num1 = st.number_input("Enter number 1")
    num2 = st.number_input("Enter number 2")
    submit_button = st.form_submit_button(label="Submit")

if submit_button:
    if choice == "Convert number to log form":
        if num1 and num2 > 0:
            num1_log = np.log(num1)
            num2_log = np.log(num2)

            st.markdown("## Result:")
            st.write("Number 1 in original number: ", num1)
            st.write("Number 2 in original number: ", num2)
            st.write("Number 1 in numpy log form: ", round(num1_log,2))
            st.write("Number 2 in numpy log form: ", round(num2_log,2))
    elif choice == "Convert log form to number":
        if num1 and num2 > 0:
            num1_exp = np.exp(num1)
            num2_exp = np.exp(num2)

            st.markdown("## Result:")
            st.write("Number 1 in numpy log form: ", num1)
            st.write("Number 2 in numpy log form: ", num2)
            st.write("Number 1 in original number: ", round(num1_exp,2))
            st.write("Number 2 in original number: ", round(num2_exp,2))
