import streamlit as st

st.markdown("""
    <style>
    /* 1. Importar la fuente JetBrains Mono (La mejor para software) */
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;600&display=swap');

    /* 2. Aplicar la fuente a TODO el sitio */
    html, body, [class*="css"], h1, h2, h3, p, div, button {
        font-family: 'JetBrains Mono', monospace !important;
    }

    /* 3. Fondo Gradiente para toda la app y la barra lateral */
    .stApp, [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #050505 0%, #0d1117 100%);
        background-attachment: fixed;
    }

    /* 4. Quitar bordes para un look minimalista */
    [data-testid="stSidebar"] > div:first-child {
        border-right: none !important;
    }
    
    /* 5. Asegurar que los botones se vean bien con la nueva fuente */
    button {
        font-weight: 600 !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.set_page_config(layout="wide", page_title="FireBlack/ChessForuming", initial_sidebar_state="collapsed", page_icon="🐦‍🔥")

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
            with st.spinner("¿Sabias que puedes comunicarte con usuarios reales aqui dentro?"):
                st.session_state.alias = ""
                st.rerun()

# Navegación
inicio = st.Page("paginas/Inicio.py", title="Inicio", icon="🐦‍🔥")
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