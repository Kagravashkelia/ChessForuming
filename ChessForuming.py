import streamlit as st

st.set_page_config(layout="wide", page_title="ChessForuming")

# Manejo global de alias
if "alias" not in st.session_state:
    st.session_state.alias = ""

# Sidebar para el Alias (siempre visible)
with st.sidebar:
    st.title("👤 Usuario")
    if not st.session_state.alias:
        st.session_state.alias = st.text_input("Elige tu alias:")
    else:
        st.write(f"Hola, **{st.session_state.alias}**")
        if st.button("Cambiar alias"):
            st.session_state.alias = ""
            st.rerun()

# Navegación
inicio = st.Page("paginas/Inicio.py", title="Inicio", icon="🏠")
crear_idea = st.Page("paginas/CrearIdea.py", title="Crear post", icon="🐦‍🔥")

nav = st.navigation([inicio, crear_idea])
nav.run()