import pandas as pd
import streamlit as st
import plotly.graph_objects as go

vehicles = pd.read_csv('vehicles_us.csv')

st.header("Analisis de datos ventas de vehiculos")



hist_button = st.button('construir histograma')
disp_button = st.button('construir grafico de dispersion')

if hist_button:
    st.write("construccion del histograma para el conjunto de datos")
    fig = go.Figure(data = [go.Histogram(x = vehicles['odometer'])])
    fig.update_layout(title_text = 'Distribucion del Odometro')
    st.plotly_chart(fig, use_container_width=True)

if disp_button:
    st.write("construccion del grafico de dispersion para el conjunto de datos")
    fig = go.Figure(data = [go.Scatter(x = vehicles['odometer'], y = vehicles['price'], mode ='markers')])
    fig.update_layout(title_text = 'Relacion entre Odometro y Precio')
    st.plotly_chart(fig, use_container_width=True)
