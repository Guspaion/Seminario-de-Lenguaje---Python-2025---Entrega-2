# Guía de instalación para ejecución de los programas

Este proyecto utiliza Jupyter Notebook para la ejecución de los archivos `.ipynb`, que a su vez dependen de funciones definidas en `functions.py`.

## Requisitos Previos

Para asegurarse de que el proyecto funciones se debe contar con lo siguiente:

- Python 3.8 o superior
- pip
- Jupyter Notebook

## Instalación

Siga estos pasos para instalar el entorno de trabajo:

1. Clona el repositorio con el siguiente comando:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
   ```
2. Instala las dependencias requeridas ejecutando:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

1. Iniciar Jupyter Notebook con:
   ```bash
   jupyter notebook
   ```
2. Desde la interfaz de Jupyter puede ingresar a la carpeta notebooks, abra el archivo que desee y ejecute la celda para utilizar el programa.

## Notas Importantes

- Si los pasos se siguieron correctamente debería tener dos carpetas en la interfaz de Jupyter, 'notebooks' y 'src', donde encontrara los `.ipynb` y el archivo `functions.py`respectivamente
- `functions.py` debe encontrarse en el mismo directorio que el notebook para su correcta importación.
