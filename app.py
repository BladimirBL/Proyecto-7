import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv("notebooks/vehicles_us.csv")


car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.write("Selecciona una o más visualizaciones para explorar el dataset de vehículos usados.")

st.header('Análisis de vehículos en EE.UU.')
button = st.checkbox('Mostrar datos')

if button:
    fig= px.histogram(car_data, x="odometer", nbins=50, title='Histograma del kilometraje de vehículos')

    st.write("Histograma de la variable 'odometer':")
    st.plotly_chart(fig)
    
st.divider()

another_button = st.checkbox('Grafico de dispersión')

if another_button:
    fig2 = px.scatter(car_data, x="model_year", y="odometer", title='Gráfico de dispersión del año vs. kilometraje')
    
    st.write("Gráfico de dispersión del año vs. kilometraje:")
    st.plotly_chart(fig2)