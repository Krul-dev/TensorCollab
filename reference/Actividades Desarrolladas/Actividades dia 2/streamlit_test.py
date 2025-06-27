import streamlit as st

st.title("Múltiples barras de progreso")

st.progress(0.3)  # 30%
st.progress(0.7)  # 70%

st.title("Progreso de tareas")
if st.button("Click me!"):
    st.write("You clicked!")
