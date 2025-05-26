#Importamos librerias

import streamlit as st
import json
from streamlit_lottie import st_lottie

def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)
    
#Creamos la informacion que se va a ver en la pagina
st.title("Sobre nosotros")

col1,col2 = st.columns(2)

with col1:
    lottie_confuse = load_lottiefile("./animaciones/Animacion 3.json")
    st_lottie(
    lottie_confuse,
    speed=1,
    reverse=False,
    loop=True,
    quality="low",
    height=300,
    width=400,
    key=None,
    )

with col2:
    st.write(
    """
    Nosotros somos estudiantes que hacen parte de la carrera de Ingenieria en la universidad San buena aventura,
    con esta pagina buscamos el objetivo de dos cosas, la primera, que mucha gente pueda a llegar a conocer y entender un poco mas el
    mundo de la programacion y como segundo objetivo el de mejorar nosotros tambien en lo que es la programacion, por eso
    nos propusimos crear este proyecto.
    """
    )


st.write(
        """
        Hablando de nuestra universidad, es una destacada por su logros y sus maestros los cuales son profesionales por no decir 
        los mejores en su ambito, Una gran universidad que cumple las expectativas de cada estudiantes.
        """
)


col1,col2,col3 = st.columns(3)
with col1:
    st.write("")
with col2:
    st.image("./imagenes/logo.jpg",width=500)
with col3:
    st.write("")