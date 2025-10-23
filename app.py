import streamlit as st

st.set_page_config(page_title="🎬 Crítico de Cine Mejorado", page_icon="🍿")

st.title("🍿 Crítico de Cine — ¿Qué tan buena fue la película?")
st.markdown("""
Escribe tu opinión sobre una película y este analizador detectará si tu comentario es **positivo, negativo o neutral**,  
basado en palabras comunes del lenguaje cotidiano del cine.  
No necesitas instalar nada adicional.
""")

# Entrada del usuario
opinion = st.text_area("🎥 Escribe tu opinión sobre una película:", height=200, placeholder="Ejemplo: 'Muy mala la película, no me gustó para nada.'")

# Listas de palabras clave
positivas = ["buena", "excelente", "increíble", "genial", "me encantó", "fascinante", "divertida", "impresionante", "maravillosa", "emocionante", "perfecta", "fantástica"]
negativas = ["mala", "horrible", "aburrida", "lenta", "terrible", "decepcionante", "fea", "desagradable", "pésima", "asco", "no me gustó", "odiosa"]

def analizar_opinion(texto):
    texto = texto.lower()
    puntos_positivos = sum(palabra in texto for palabra in positivas)
    puntos_negativos = sum(palabra in texto for palabra in negativas)
    
    if puntos_positivos > puntos_negativos:
        return "positiva", puntos_positivos - puntos_negativos
    elif puntos_negativos > puntos_positivos:
        return "negativa", puntos_negativos - puntos_positivos
    else:
        return "neutral", 0

if st.button("Analizar opinión"):
    if opinion.strip():
        tipo, intensidad = analizar_opinion(opinion)

        st.markdown("---")
        st.markdown("## 🎭 Resultado del análisis")

        if tipo == "positiva":
            st.success("🎉 Opinión positiva — ¡Te gustó la película!")
            st.info(f"Nivel de entusiasmo: {intensidad}")
            st.balloons()
        elif tipo == "negativa":
            st.error("💀 Opinión negativa — Parece que no te gustó mucho.")
            st.info(f"Nivel de desagrado: {intensidad}")
        else:
            st.warning("😐 Opinión neutral — No expresas emociones fuertes.")
        
        # Veredicto final
        st.markdown("### 📊 Veredicto final:")
        if tipo == "positiva":
            st.success("Recomiendas esta película 🍿")
        elif tipo == "negativa":
            st.error("No la recomendarías 👎")
        else:
            st.warning("No tienes una opinión clara 🤔")
    else:
        st.warning("Por favor, escribe una opinión para analizar.")

st.markdown("---")
st.caption("🎬 Desarrollado con ❤️ — Analiza tus críticas de cine de forma natural y rápida.")

