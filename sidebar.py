#Importamos librerias
import streamlit as st

#Condiguracion de sidebar para incluir cada app de steamlib

sobrenosotros = st.Page(
    page="paginas/app.py",
    title = "Quienes somos",
    icon = "",
    default = True,
)

javascript = st.Page(
    page = "paginas/app2.py",
    title = "Aprende sobre java",
    icon=":material/bar_chart:",
    
)

bienvenida = st.Page(
    page = "paginas/app0.py",
    title="Bienvenido a nuestra pagina",
    icon=""
)

aprende_c = st.Page(
    page = "paginas/app3.py",
    title= "Aprende C++",
    icon=":material/computer:",
)

aprende_python = st.Page(
    page = "paginas/app4.py",
    title= "Aprende Python",
    icon=":material/smart_toy:",
)


#Navegacion
navegation = st.navigation(
    {
        "Informacion": [bienvenida,sobrenosotros],
        "Lenguajes":[javascript,aprende_c,aprende_python],
    }
)

#Informacion de sidebar y ejecucion

st.sidebar.text("Pagina para aprender a programar 🖥️")
navegation.run()