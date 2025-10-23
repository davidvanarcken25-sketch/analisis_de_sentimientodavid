import streamlit as st
from textblob import TextBlob
import re

st.set_page_config(
    page_title="🧠 Analizador de Mensajes",
    page_icon="💬",
    layout="wide"
)

st.title("💬 Analizador de Mensajes — ¿Qué dice tu texto de ti?")
st.markdown("""
Escribe cómo te sientes o cualquier texto, y descubre si transmite un tono **positivo, negativo o neutral**,  
además de qué tan **emocional o racional** es tu mensaje.
""")

# Entrada de texto
st.subheader("✍️ Escribe algo para analizar")
texto = st.text_area("Por ejemplo: 'Hoy fue un gran día, me siento increíblemente motivado.'", height=200)

# Botón para analizar
if st.button("Analizar texto"):
    if texto.strip():
        try:
            # Traducción automática al inglés para mejor análisis
            blob_es = TextBlob(texto)
            texto_en = str(blob_es.translate(to='en'))
        except Exception:
            texto_en = texto  # Si falla la traducción, usa el texto original

        blob = TextBlob(texto_en)
        sentimiento = blob.sentiment.polarity
        subjetividad = blob.sentiment.subjectivity

        palabras = re.findall(r'\b\w+\b', texto.lower())
        palabras_unicas = set(palabras)
        total_palabras = len(palabras)
        total_unicas = len(palabras_unicas)

        st.subheader("📊 Resultados del análisis")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🎭 Sentimiento")
            sentimiento_norm = (sentimiento + 1) / 2
            st.progress(sentimiento_norm)

            if sentimiento > 0.1:
                st.success(f"Mensaje Positivo ({sentimiento:.2f}) 😊")
            elif sentimiento < -0.1:
                st.error(f"Mensaje Negativo ({sentimiento:.2f}) 😟")
            else:
                st.info(f"Mensaje Neutral ({sentimiento:.2f}) 😐")

        with col2:
            st.markdown("### 💭 Subjetividad")
            st.progress(subjetividad)
            if subjetividad > 0.5:
                st.warning(f"Alta subjetividad ({subjetividad:.2f}) — muy emocional")
            else:
                st.info(f"Baja subjetividad ({subjetividad:.2f}) — más racional")

        st.subheader("🧩 Métricas del texto")
        st.write(f"- Total de palabras: **{total_palabras}**")
        st.write(f"- Palabras únicas: **{total_unicas}**")
        st.write(f"- Porcentaje de palabras únicas: **{(total_unicas / total_palabras * 100):.1f}%**")

        palabras_largas = [p for p in palabras if len(p) > 6]
        if palabras_largas:
            st.write("🔍 Palabras destacadas:", ", ".join(sorted(set(palabras_largas))[:10]))

    else:
        st.warning("Por favor, escribe algo para analizar.")

st.markdown("---")
st.caption("Desarrollado con ❤️ usando Streamlit y TextBlob — ahora entiende tus emociones en español.")
