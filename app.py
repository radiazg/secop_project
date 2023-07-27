import streamlit as st
from joblib import load
import numpy as np

# Carga del modelo previamente guardado


def load_model():
    model = load('Secop_pipeline.joblib')
    return model



model = load_model()

st.title('Mi Aplicación de Predicción')

st.write('Por favor, introduce los datos para la predicción')


opciones = ["Distrito Capital de Bogotá", "Valle del Cauca", "Antioquia", "Santander", "Meta", "Boyacá", "Risaralda", "Cundinamarca", "Huila", "Casanare"]
departamento = st.selectbox('Departamento:', opciones)
opciones = ['Territorial','Nacional','Corporación Autónoma']
orden = st.selectbox('Orden:', opciones)
opciones = ['Decscentralizada','Centralizada']
entidadCentralizada = st.selectbox('Entidad Centralizada:', opciones)
opciones = ['Contratación directa','Contratación régimen especial','Mínima cuantía','Selección Abreviada de Menor Cuantía','Selección abreviada subasta inversa','Contratación Directa (con ofertas)']
modalidadContratacion = st.selectbox('Modalidad de Contratación:', opciones)
opciones = ['Inversión','Funcionamiento']
destinoGasto = st.selectbox('Destino Gasto:', opciones)
opciones = ['Hombre', 'Mujer', 'No Definido', 'Otro']
generoRepresentante = st.selectbox('Genero Representante:', opciones)

esServicioPublico = st.checkbox('Es servicio publico')
esRecursosPropios = st.checkbox('Es recursos propios')
esGrupo = st.checkbox('Es grupo')
esPrestacionServicios = st.checkbox('Es prestacion de servicios')
esPyme = st.checkbox('Es  Pyme')
estaLiquidado = st.checkbox('Esta liquidado')
esObligacionAmbiental = st.checkbox('Es obligacion ambiental')
esPostconflicto = st.checkbox('Es post conflicto')

diasAdicionados = st.number_input('Dias adicionados', step=1)
valorContrato = st.number_input('Valor del contrato', min_value=0, step=1)
valorFacturado = st.number_input('Valor facturado', min_value=0, step=1)
valorPendientePago = st.number_input('Valor pendiente de pago', min_value=0, step=1)
saldoCDP = st.number_input('Saldo CDP', min_value=0, step=1)



# Crear el botón de predicción
pred_button = st.button('Predecir')



# Cuando el usuario haga click en el botón 'Predecir', obtén la predicción del modelo y muéstrala.
if pred_button:
    datos = np.array([departamento, orden, entidadCentralizada,modalidadContratacion, destinoGasto, generoRepresentante, esServicioPublico, esRecursosPropios, esGrupo, esPrestacionServicios, esPyme  , estaLiquidado, esObligacionAmbiental, esPostconflicto, diasAdicionados, valorContrato, valorFacturado, valorPendientePago, saldoCDP]).reshape(1,-1)
    prediccion = model.predict(datos)

    st.write('La predicción del modelo es: ', prediccion)
