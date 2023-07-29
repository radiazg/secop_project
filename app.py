import pandas as pd
import streamlit as st
from joblib import load
import numpy as np
from PIL import Image

# Carga del modelo previamente guardado


def load_model():
    model = load('Secop_pipeline.joblib')
    return model



model = load_model()

st.title('SECOP - Predicción de Contratos Cerrados')
st.markdown('### Por favor, introduce los datos para la predicción')
st.write("")

col1, col2, col3 = st.columns(3)

# Col1 con Seleccion de Opciones de Contrato
with col1:
    st.markdown('**Seleccionar Opciones**')
    opciones = ["Distrito Capital de Bogotá", "Valle del Cauca", "Antioquia", "Santander", "Meta", "Boyacá", "Risaralda", "Cundinamarca", "Huila", "Casanare"]
    departamento = st.selectbox('Departamento:', opciones)
    opciones = ['Territorial','Nacional','Corporación Autónoma']
    orden = st.selectbox('Orden:', opciones)
    opciones = ['Descentralizada','Centralizada']
    entidadCentralizada = st.selectbox('Entidad Centralizada:', opciones)
    opciones = ['Contratación directa','Contratación régimen especial','Mínima cuantía','Selección Abreviada de Menor Cuantía','Selección abreviada subasta inversa','Contratación Directa (con ofertas)']
    modalidadContratacion = st.selectbox('Modalidad de Contratación:', opciones)
    opciones = ['Inversión','Funcionamiento']
    destinoGasto = st.selectbox('Destino Gasto:', opciones)
    opciones = ['Hombre', 'Mujer', 'No Definido', 'Otro']
    generoRepresentante = st.selectbox('Genero Representante:', opciones)

# Col2 con Definiones de tipo de contrato
with col2:
    st.markdown('**Definir Tipo**')
    esServicioPublico = st.checkbox('Es servicio publico')
    esRecursosPropios = st.checkbox('Es recursos propios')
    esGrupo = st.checkbox('Es grupo')
    esPrestacionServicios = st.checkbox('Es prestacion de servicios')
    esPyme = st.checkbox('Es  Pyme')
    estaLiquidado = st.checkbox('Esta liquidado')
    esObligacionAmbiental = st.checkbox('Es obligacion ambiental')
    esPostconflicto = st.checkbox('Es post conflicto')

# Col3 con Valores del COntrato
with col3:
    st.markdown('**Valores del Contrato**')
    diasAdicionados = st.number_input('Dias adicionados', step=1)
    valorContrato = st.number_input('Valor del contrato', min_value=0, step=1)
    valorFacturado = st.number_input('Valor facturado', min_value=0, step=1)
    valorPendientePago = st.number_input('Valor pendiente de pago', min_value=0, step=1)
    saldoCDP = st.number_input('Saldo CDP', min_value=0, step=1)

# Crear el botón de predicción
pred_button = st.button('Predecir')



# Cuando el usuario haga click en el botón 'Predecir', obtén la predicción del modelo y muéstrala.
if pred_button:
    datos = pd.DataFrame([[departamento, orden, entidadCentralizada,modalidadContratacion, destinoGasto, generoRepresentante, esServicioPublico, esRecursosPropios, esGrupo, esPrestacionServicios, esPyme  , estaLiquidado, esObligacionAmbiental, esPostconflicto, diasAdicionados, valorContrato, valorFacturado, valorPendientePago, saldoCDP]], columns=['Departamento','Orden','Entidad Centralizada','Modalidad de Contratacion','Destino Gasto','Género Representante Legal','EsServicioPublico','EsRecursosPropios','EsGrupo','EsPrestacionServicios','EsPyme','EstaLiquidado','EsObligacionAmbiental','Es PostConflicto','Dias Adicionados','Valor del Contrato','Valor Facturado','Valor Pendiente de Pago','Saldo CDP'])
    prediccion = model.predict_proba(datos)

    st.markdown('#### La probabilidad que el contrato se cierre es de: {:.1%}'.format(prediccion[0][1]))
