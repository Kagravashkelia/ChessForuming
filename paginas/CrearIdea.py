import streamlit as st
from db import supabase

st.title("Crear un nuevo post 🐦‍🔥")

if not st.session_state.alias:
    st.warning("⚠️ Debes configurar un alias en el menú lateral para publicar.")
    st.stop()

# ESTO ES LO IMPORTANTE: Todo lo de abajo debe estar indentado
with st.form("form_post"):
    titulo = st.text_input("Título de tu idea")
    contenido = st.text_area("Explica tu idea...")
    
    # El botón DEBE estar aquí adentro
    enviar = st.form_submit_button("Publicar")

# El 'if' va afuera del 'with', pero el botón ya fue definido arriba
if enviar:
    if titulo and contenido:
        try:
            supabase.table("posts").insert({
                "titulo": titulo, 
                "contenido": contenido, 
                "autor": st.session_state.alias
            }).execute()
            st.success("¡Publicado!")
            st.rerun() # Para que se recargue y se vea el nuevo post
        except Exception as e:
            st.error(f"Error: {e}")