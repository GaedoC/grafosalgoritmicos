# grafos-punto-jota-pe-ge
## API REST
API en Flask para manejar grafos. Requiere Python 3 y una versión compatible de PIP. Para levantar el servicio:
* Situarse en la carpeta `servicio`.
* Crear un entorno virtual de Python (recomiendo virtualenv: `virtualenv -p [ruta de Python3] venv`).
* En la línea de comandos, ejecutar `pip install -r requirements.txt`.
* Ejecutar `python index.py` y el servicio estará disponible en `http://localhost:5151/`

Nótese que si se tiene instalado Python2 y Python3 simultáneamente (como en sistemas Linux), el comando `python` se reemplaza por `python3` y `pip` por `pip3`.