import streamlit as st
from db import supabase

st.title("Crear un nuevo post 🐦‍🔥")

if not st.session_state.alias:
    st.warning("⚠️ Debes configurar un alias en el menú lateral para publicar.")
    st.stop()

# Ejemplo de cómo prohibir a alguien
def es_usuario_baneado(alias):
    baneados = supabase.table("banned_users").select("alias").eq("alias", alias).execute().data
    return len(baneados) > 0

# En tu código de publicar:
if st.form_submit_button("Publicar"):
    if es_usuario_baneado(st.session_state.alias):
        st.error("No puedes publicar, has sido baneado.")
    else:
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