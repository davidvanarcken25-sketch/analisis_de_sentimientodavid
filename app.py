import streamlit as st
from textblob import TextBlob
import re

# Configuración general
st.set_page_config(
    page_title="🧠 Analizador de Mensajes",
    page_icon="💬",
    layout="wide"
)

# Título
st.title("💬 Analizador de Mensajes — ¿Qué dice tu texto de ti?")
st.markdown("""
Escribe cualquier texto y descubre si transmite un tono **positivo, negativo o neutral**,  
además de qué tan **emocional o objetivo** es tu mensaje.
""")

# Entrada de texto
st.subheader("✍️ Escribe algo para analizar")
texto = st.text_area("Por ejemplo: 'Hoy fue un gran día, me siento increíblemente motivado.'", height=200)

# Botón para analizar
if st.button("Analizar texto"):
    if texto.strip():
        # Procesar texto
        blob = TextBlob(texto)
        sentimiento = blob.sentiment.polarity
        subjetividad = blob.sentiment.subjectivity

        # Contar palabras sin dependencias externas
        palabras = re.findall(r'\b\w+\b', texto.lower())
        palabras_unicas = set(palabras)
        total_palabras = len(palabras)
        total_unicas = len(palabras_unicas)

        # Mostrar resultados
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

        # Métricas simples del texto
        st.subheader("🧩 Métricas del texto")
        st.write(f"- Total de palabras: **{total_palabras}**")
        st.write(f"- Palabras únicas: **{total_unicas}**")
        st.write(f"- Porcentaje de palabras únicas: **{(total_unicas / total_palabras * 100):.1f}%**")

        # Mostrar palabras más largas
        palabras_largas = [p for p in palabras if len(p) > 6]
        if palabras_largas:
            st.write("🔍 Palabras destacadas:", ", ".join(sorted(set(palabras_largas))[:10]))

    else:
        st.warning("Por favor, escribe algo para analizar.")

# Pie de página
st.markdown("---")
st.caption("Desarrollado con ❤️ usando Streamlit y TextBlob — sin necesidad de instalar nada adicional.")
