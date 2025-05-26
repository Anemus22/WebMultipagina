#Importamos librerias
import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie


#Funcion necesaria para ejecutar las animaciones
def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)


#Contenido de pagina
st.title("Bienvenido a la pagina de aprendizaje")
st.write(
    """
    En esta pagina podras ver diferentes roadmaps y recursos para poder empezar tu camino como programador
    contamos con diferentes lenguajes y ayudas que te serviran durante tu camino,espero que disfrutes del proceso y empieza 😁

    """
)
#Guardamos la animacion en una variable
loattie_bienvenida = load_lottiefile("./animaciones/Animation2.json")



#Le damos los ajuste necesarios a la animacion
st_lottie(
    loattie_bienvenida,
    speed=1,
    reverse=False,
    loop=True,
    quality="low",
    height=400,
    width=700,
    key=None,
)


#Contenido de pagina
st.title("Mejora tus habilidades de programacion")
st.write(
    """
    Explorar nuevas herramientas, resolver desafíos y perfeccionar tu lógica algorítmica es importante para convertirte en un mejor programador. 
    En esta página encontrarás recursos, ejercicios y estrategias diseñadas para fortalecer tus conocimientos en Javascript, Python y C++. 
    Si buscas dominar estos campos,estás en el lugar indicado.

    """
)
