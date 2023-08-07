secop_project
==============================
## Que es el SECOP

El significado de su sigla corresponde a Sistema Electrónico de Contratación Pública, es una plataforma digital del gobierno colombiano que tiene como objetivo mejorar la transparencia y eficiencia del proceso de contratación pública en el país.

El SECOP permite a entidades estatales publicar información sobre los procesos de contratación, incluyendo licitaciones, contratos adjudicados, y otros detalles relacionados con los contratos del sector público. También permite a los proveedores registrarse y participar en estos procesos.

El sistema está diseñado para proporcionar un acceso transparente y equitativo a las oportunidades de contratación con el gobierno, permitiendo a los ciudadanos y empresas buscar y acceder a esta información de manera fácil y abierta.

Existen dos versiones de esta plataforma: SECOP I y SECOP II. SECOP I contiene la información de todos los procesos de contratación publicados hasta 2015 y SECOP II es la versión actualizada y mejorada del sistema, que empezó a utilizarse a partir de 2015 y es la que se utiliza actualmente.

## Objetivo del proyecto 

Predecir cuándo un contrato adjudicado por el estado tiene la probabilidad más alta de cerrarse, basándose en las características del contrato como el Departamento (Estado), el orden, la modalidad, el destino del gasto, entre otros aspectos relevantes de la contratación.

Es importante saber diferenciar entre un contrato cerrado y un contrato terminado. Un contrato cerrado se refiere a un contrato que ha sido ejecutado en su totalidad, liquidado y archivado. Mientras que un contrato terminado es aquel que ha sido ejecutado en su totalidad, pero aún no ha sido liquidado o archivado.

Un contrato cerrado es aquel que ha finalizado y ya no está vigente, y que las partes involucradas no pueden realizar ninguna modificación al contrato ni pueden iniciar un proceso de reclamación de daños en caso de incumplimiento de las obligaciones contractuales.

## ¿Porque es relevante esta información?

Al poder predecir la probabilidad de cierre de un contrato, los entes de control podrían poner la lupa, sobre todos aquellos contratos que tengan una probabilidad de cierre baja para poder tomar decisiones de manera anticipada, y poder mitigar posibles riesgos o corregir acciones para incrementar esta probabilidad de que culmine satisfactoriamente.

## Requisitos y dependencias

- streamlit==1.25.0
- pandas==2.0.3
- joblib==1.3.1
- scikit-learn==1.3.0
- numpy==1.25.1
- Pillow==9.5.0

## Información sobre los datos utilizados para el entrenamiento.

Los datos fuente fueron descargados del portal de Datos Abiertos del Gobierno de Colombia que están disponible a todo el público.
https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Contratos-Electr-nicos/jbjy-vk9h
El archivo original pesa 3.62 Gb, por lo tanto, este archivo fue procesado inicialmente para descartar varias columnas de datos que no eran relevante para nuestra predicción y fue realizado en el notebook Filtrado_datos_secop generando un archivo ideal (datos_filtradosv1.csv) para iniciar con el tratamiento de datos.

Para ejecutar el notebook debe descargar el archivo fuente y dejarlo en la carpeta data/raw

Diccionario de datos
https://www.datos.gov.co/api/views/jbjy-vk9h/files/839439f9-b3b9-4e53-a28d-ab82e752a1dc?download=true&filename=Diccionario%20de%20Datos%20Abiertos%202022%20Contratos%20Electronicos.pdf

### Instalar librerías requeridas para el proyecto

Antes de instalar las librerías, debe generar un entorno virtual de python como buena práctica.  A continuación en nuestro terminal ejecutamos:

```
python3 -m venv venv
```

Inicializar el entrono virtual

```
source venv/bin/activate
```

Luego instalar las librerías

```
pip install -r requirements.txt
```

## Generar Modelo

Una vez instalado las librerías necesarias, debe ejecutar el notebook `Secop.ipynb` que se encuantra en la carpeta `notebooks`

Este notebook genera un archivo .joblib en la carpeta `models`, debe copiar este archivo y pegarlo en el path principal del proyecto al nivel del archivo `app.py`

## Lanzar la web app de Streamlit

En el terminal debemos ejecutar

```
streamlit run app.py
```

## Organización del proyecto


    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── app.py             <- Aplicacion de streamlit
    ├── README.md          <- README para los desarrolladores que usen este proyecto
    ├── data
    │   ├── external       <- Datos de sitios de terceros
    │   ├── interim        <- Datos intermedios que han sido transformados
    │   ├── processed      <- El final, datos que fueron utilizados para el desarrollo del modelo
    │   └── raw            <- El archivo original de los datos
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Modelos entrenados y serializados, predicciones de modelos, o resúmenes de modelos.
    │
    ├── notebooks          <- Jupyter notebooks.
    │
    ├── references         <- Diccionarios de datos, manuales y todos los demás materiales explicativos.
    │
    ├── reports            <- Analisis generados como HTML, PDF, LaTeX, etc.
    │   └── figures        <- Graficas y figuras generadas para los reportes
    │
    ├── requirements.txt   <- El archivo de requerimientos para generar el ambiente
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Código fuente del proyecto
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts para descargar o generar los datos
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts para convertir los datos planos en caracteristicas para el modelamiento
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts para entrenar los modelos y luego usar los modelos entrenados para realizar predicciones
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts para crear las visualizaciones para la exploración y los resultados
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io




--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
