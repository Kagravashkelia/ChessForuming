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
            # SOLO MUESTRA EL BOTÓN DE BORRAR SI ERES ADMIN
            if st.session_state.is_admin:
                if st.button("🗑️ Eliminar Post", key=f"del_post_{post['id']}"):
                    with st.spinner("Borrando..."):
                        supabase.table("posts").delete().eq("id", post['id']).execute()
                        st.rerun()

            # Sección de comentarios
            st.divider()
            st.write("💬 Respuestas:")
            comentarios = supabase.table("comentarios").select("*").eq("post_id", post['id']).execute().data
            
            for com in comentarios:
                # Usamos columnas para alinear el mensaje y el botón de borrar
                c1, c2 = st.columns([0.8, 0.2])
                with c1:
                    st.markdown(f"**{com['autor']}**: {com['contenido']}")
                with c2:
                    # CLAVE AQUÍ: key único usando 'del_com' para no chocar con 'del_post'
                    if st.button("🗑️", key=f"del_com_{com['id']}"):
                        # CORRECCIÓN AQUÍ: eq("id", ...) porque borramos por ID del comentario
                        supabase.table("comentarios").delete().eq("id", com['id']).execute()
                        st.rerun()
            
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