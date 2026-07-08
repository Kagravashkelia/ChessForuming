import streamlit as st
from db import supabase

st.title("Crear un nuevo post 🐦‍🔥")

if not st.session_state.alias:
    st.warning("⚠️ Debes configurar un alias en el menú lateral para publicar.")
    st.stop()

with st.form("form_post"):
    titulo = st.text_input("Título de tu idea")
    contenido = st.text_area("Explica tu idea...")
    enviar = st.form_submit_button("Publicar")

if enviar:
    if titulo and contenido:
        try:
            supabase.table("posts").insert({
                "titulo": titulo, 
                "contenido": contenido, 
                "autor": st.session_state.alias
            }).execute()
            st.success("¡Publicado!")
        except Exception as e:
            st.error(f"Error: {e}")