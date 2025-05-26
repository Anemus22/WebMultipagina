#Importamos librerias
import streamlit as st
import requests
from streamlit_lottie import st_lottie
import json

#Funcion necesaria para ejecutar las animaciones
def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)



#Contenido de pagina
st.title("Curso de Programación en Python")

st.markdown("### ¿Qué deseas hacer?")
opcion = st.selectbox("Opciones:", ["Introducción", "Ir al curso", "Práctica"])


#Guardamos el puerto donde esta alojado el curso en una variable
backend_url = "http://127.0.0.1:8080"

#Contenido de pagina que funciona segun lo que elija el usuario

if opcion == "Introducción":
    st.markdown("Bienvenido al curso básico de programación de Python")
    st.markdown("Este curso tiene niveles y diferentes recursos que te perimitiran saber lo basico de Python")
    st.video("https://www.youtube.com/watch?v=ArPZTY3dRhg")

elif opcion == "Ir al curso":
    st.info("Haz clic abajo para abrir el curso completo.")
    st.markdown(f"[Abrir Curso]({backend_url})")
    lottie_python = load_lottiefile("./animaciones/Animation4.json")
    st_lottie(
    lottie_python,
    speed=2,
    reverse=False,
    loop=True,
    quality="low",
    height=400,
    width=700,
    key=None,
    )

elif opcion == "Práctica":
    st.info("Puedes ir directamente a la práctica final.")
    st.markdown(f"[Abrir Práctica]({backend_url}/practice)")
    lottie_python = load_lottiefile("./animaciones/Animation4.json")
    st_lottie(
    lottie_python,
    speed=2,
    reverse=False,
    loop=True,
    quality="low",
    height=400,
    width=700,
    key=None,
    )

#Anuncio para ejecutar el codigo necesario para el curso
st.warning("⚠️ Importante ejecutar flask en una terminal con el codigo = python.py desde la carpte Flask")