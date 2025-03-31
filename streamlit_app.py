import streamlit as st

st.title("AI Tester")

with st.container(border=True):

    prompt = st.selectbox(
    "Versión",
    ("v1.0.0 (20250331)", "v1.1.0 (20250403)", "v1.2.0 (20250410)", "prueba Aleix", "prueba Zigor"),
    )

    optinGlosario = st.checkbox("Glosario terminológico")

    optinTDB = st.checkbox("Technical Database")

with st.container(border=True):
    
    prompt = st.chat_input("Consulta técnica...")

    st.button("Enviar", key=1)

with st.container(border=True):

    st.text("Aquí se inyectaría la respuesta a la pregunta...")
    st.text("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

with st.container(border=True):

    st.write("Feedback")
    st.feedback("thumbs")

    prompt = st.chat_input("Comentarios...")
    
    st.button("Enviar", key=2)