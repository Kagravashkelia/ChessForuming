import streamlit as st
from db import supabase

st.title("ChessForuming 🐦‍🔥")

if not st.session_state.alias:
    st.warning("⚠️ Por favor, escribe un alias en el menú de la izquierda para ver y comentar posts.")
    st.stop()

# Consultar posts
try:
    response = supabase.table("posts").select("*").order("created_at", desc=True).execute()
    posts = response.data

    if not posts:
        st.info("No hay posts aún.")

    for post in posts:
        with st.container(border=True):
            st.subheader(post['titulo'])
            st.write(post['contenido'])
            st.caption(f"Publicado por: {post['autor']}")
            
            # Botón de eliminar
            if st.button("🗑️ Eliminar", key=f"del_{post['id']}"):
                supabase.table("posts").delete().eq("id", post['id']).execute()
                st.rerun()

            # Sección de comentarios
            st.divider()
            st.write("💬 Respuestas:")
            comentarios = supabase.table("comentarios").select("*").eq("post_id", post['id']).execute().data
            for com in comentarios:
                st.markdown(f"**{com['autor']}**: {com['contenido']}")
            
            # Formulario para nuevo comentario
            with st.form(key=f"form_{post['id']}", clear_on_submit=True):
                respuesta = st.text_input("Tu respuesta:")
                if st.form_submit_button("Responder"):
                    if respuesta:
                        supabase.table("comentarios").insert({
                            "post_id": post['id'],
                            "contenido": respuesta,
                            "autor": st.session_state.alias
                        }).execute()
                        st.rerun()
except Exception as e:
    st.error(f"Error: {e}")