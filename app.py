import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="🎬 Crítico de Cine", page_icon="🍿")

st.title("🍿 Crítico de Cine — ¿Qué tan buena fue la película?")
st.markdown("""
Escribe tu opinión sobre una película y este analizador detectará si tu comentario es **positivo, negativo o neutral**,  
además de mostrarte qué tipo de crítica estás haciendo.
""")

# Entrada del usuario
opinion = st.text_area("🎥 Escribe tu opinión sobre una película:", height=200, placeholder="Ejemplo: 'La historia de Dune es impresionante, me encantó.'")

if st.button("Analizar opinión"):
    if opinion.strip():
        try:
            # Traducir al inglés (TextBlob funciona mejor así)
            blob_es = TextBlob(opinion)
            opinion_en = str(blob_es.translate(to='en'))
        except Exception:
            opinion_en = opinion  # Si no puede traducir, usa el texto original

        blob = TextBlob(opinion_en)
        polaridad = blob.sentiment.polarity
        subjetividad = blob.sentiment.subjectivity

        # Determinar sentimiento
        if polaridad > 0.1:
            resultado = "🎉 Opinión positiva — ¡Te gustó la película!"
            color = "success"
        elif polaridad < -0.1:
            resultado = "💀 Opinión negativa — Parece que no te gustó mucho."
            color = "error"
        else:
            resultado = "😐 Opinión neutral — No expresas emociones fuertes."
            color = "info"

        # Mostrar resultados
        st.markdown("---")
        st.markdown("## 🎭 Resultado del análisis")
        getattr(st, color)(resultado)

        st.markdown("### 📊 Detalles del análisis:")
        st.write(f"- **Polaridad:** {polaridad:.2f} (entre -1 = muy negativa y +1 = muy positiva)")
        st.write(f"- **Subjetividad:** {subjetividad:.2f} (entre 0 = objetiva y 1 = emocional)")

        # Tipo de comentario
        if subjetividad > 0.6:
            tipo = "emocional (hablas desde tus sentimientos)"
        elif subjetividad < 0.3:
            tipo = "objetiva (analizas hechos concretos)"
        else:
            tipo = "mixta (mezcla de emociones y razonamiento)"

        st.info(f"Tu crítica parece **{tipo}**.")

        # Frase final interpretando el resultado
        if polaridad > 0.1:
            st.success("Veredicto final: ¡Recomiendas esta película! 🍿")
        elif polaridad < -0.1:
            st.error("Veredicto final: No la recomendarías. 👎")
        else:
            st.warning("Veredicto final: No tienes una opinión clara al respecto. 🤔")

    else:
        st.warning("Por favor, escribe una opinión para analizar.")

st.markdown("---")
st.caption("Desarrollado con ❤️ por tu asistente de cine — analiza tus reseñas como un crítico profesional.")



