import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv(
    'vehicles_us.csv')  # Load data
hist_button = st.button('Construir histograma')  # Button to build histogram
# Button to build scatterplot
scatter_button = st.button('Construir grafico de dispersion')

if hist_button:
    st.write('Creacion de un histograma para el conjunto de datos de anuncios de venta de autos en EE. UU.')  # Title

    fig = px.histogram(car_data, x='odometer')  # Create histogram

    st.plotly_chart(fig, use_container_width=True)  # Show histogram

if scatter_button:
    st.write('Creacion de un grafico de dispersion para el conjunto de datos de anuncios de venta de autos en EE. UU.')  # Title

    fig = px.scatter(car_data, x='odometer', y='price')  # Create scatterplot

    st.plotly_chart(fig, use_container_width=True)  # Show scatterplot
