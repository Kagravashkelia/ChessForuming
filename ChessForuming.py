import streamlit as st

st.set_page_config(layout="wide", page_title="ChessForuming")

# --- INICIALIZACIÓN ---
if "alias" not in st.session_state:
    st.session_state.alias = ""

if "is_admin" not in st.session_state:
    st.session_state.is_admin = False
# ----------------------

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

# Inicializar estado de admin
if "is_admin" not in st.session_state:
    st.session_state.is_admin = False

with st.sidebar:
    # ... (tu código anterior de Alias)
    
    st.divider()
    st.subheader("🛠️ Panel Admin")
    if not st.session_state.is_admin:
        admin_pass = st.text_input("Clave Admin", type="password")
        if st.button("Activar Admin"):
            if admin_pass == st.secrets["ADMIN_PASS"]:
                st.session_state.is_admin = True
                st.rerun()
            else:
                st.error("Clave incorrecta")
    else:
        st.success("Modo Admin activado")
        if st.button("Desactivar Admin"):
            st.session_state.is_admin = False
            st.rerun()