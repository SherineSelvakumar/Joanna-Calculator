import streamlit as st
st.title("Joanna's Calculator")
st.write("This is a Calculator app built with Python Streamlit for Joanna -II D")

st.text_input("Enter first number", key="num1")
st.text_input("Enter second number", key="num2")

st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"], key="operation")

if st.button("Calculate"):
    num1 = float(st.session_state.num1)
    num2 = float(st.session_state.num2)
    operation = st.session_state.operation

    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Invalid operation"

    st.write(f"Result: {result}")

st.write("Thank you, Friends! - From Joanna")