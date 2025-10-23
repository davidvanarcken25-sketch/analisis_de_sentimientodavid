import streamlit as st
import pandas as pd
from textblob import TextBlob
import re

# Configuración de la página
st.set_page_config(
    page_title="🎬 Analizador de Opiniones de Películas",
    page_icon="🎥",
    layout="wide"
)

# Título y descripción
st.title("🍿 Analizador de Opiniones de Películas")
st.markdown("""
Esta aplicación analiza opiniones o reseñas sobre películas.  
Podrás conocer:
- Si el comentario tiene un tono **positivo, negativo o neutral**  
- Qué tan **subjetiva** es la opinión  
- Las **palabras más frecuentes** en tus reseñas
""")

# Barra lateral
st.sidebar.title("Opciones de Entrada")
modo = st.sidebar.selectbox(
    "Selecciona cómo quieres ingresar el texto:",
    ["Escribir opinión", "Subir archivo de texto"]
)

# Función para contar palabras (sin NLTK)
def contar_palabras(texto):
    stop_words = set([
        "a", "de", "la", "el", "que", "y", "en", "es", "un", "una", "por", "con",
        "para", "los", "las", "se", "del", "al", "como", "su", "lo", "muy", "me", 
        "mi", "yo", "tú", "te", "le", "les", "o", "no", "sí", "ya", "pero", "más",
        "cuando", "qué", "donde", "si", "sin", "todo", "todos", "esa", "ese", "esa"
    ])
    palabras = re.findall(r'\b\w+\b', texto.lower())
    palabras_filtradas = [p for p in palabras if p not in stop_words and len(p) > 2]
    contador = {}
    for palabra in palabras_filtradas:
        contador[palabra] = contador.get(palabra, 0) + 1
    contador_ordenado = dict(sorted(contador.items(), key=lambda x: x[1], reverse=True))
    return contador_ordenado

# Función para procesar texto
def procesar_texto(texto):
    blob = TextBlob(texto)
    sentimiento = blob.sentiment.polarity
    subjetividad = blob.sentiment.subjectivity
    contador_palabras = contar_palabras(texto)
    return sentimiento, subjetividad, contador_palabras

# Función para mostrar resultados
def mostrar_resultados(sentimiento, subjetividad, contador_palabras, texto):
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎭 Análisis de Sentimiento")
        st.write(f"**Texto analizado:** {texto[:150]}{'...' if len(texto) > 150 else ''}")
        
        sentimiento_norm = (sentimiento + 1) / 2
        st.progress(sentimiento_norm)
        
        if sentimiento > 0.1:
            st.success(f"Sentimiento positivo ({sentimiento:.2f})")
        elif sentimiento < -0.1:
            st.error(f"Sentimiento negativo ({sentimiento:.2f})")
        else:
            st.info(f"Sentimiento neutral ({sentimiento:.2f})")
        
        st.write("**Subjetividad:**")
        st.progress(subjetividad)
        if subjetividad > 0.5:
            st.warning(f"Alta subjetividad ({subjetividad:.2f})")
        else:
            st.info(f"Baja subjetividad ({subjetividad:.2f})")
    
    with col2:
        st.subheader("🗝️ Palabras más frecuentes")
