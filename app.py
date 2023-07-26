import streamlit as st
from joblib import load
import numpy as np

#Carga del modelo previamente guardado
def load_model():
    model = load('/models/Secop_pipeline.joblib')
    return model


model = load_model()

st.title('Mi Aplicación de Predicción')

st.write('Por favor, introduce los datos para la predicción')

# Suponemos que tu modelo usa tres variables de entrada. Modifica esto según tu modelo.
var1 = st.number_input('Introduce la variable 1')
var2 = st.number_input('Introduce la variable 2')
var3 = st.number_input('Introduce la variable 3')

# Crear el botón de predicción
pred_button = st.button('Predecir')



# Cuando el usuario haga click en el botón 'Predecir', obtén la predicción del modelo y muéstrala.
if pred_button:
    datos = np.array([var1, var2, var3]).reshape(1,-1)
    prediccion = model.predict(datos)

    st.write('La predicción del modelo es: ', prediccion)