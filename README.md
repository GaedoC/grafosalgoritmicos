# Aplicación web de algoritmos de grafos

## API REST

API en Flask para manejar grafos. Requiere Python 3 y una versión compatible de PIP. Para levantar el servicio:
* Situarse en la carpeta raíz del proyecto.
* Crear un entorno virtual de Python (recomiendo virtualenv: `virtualenv -p [ruta de Python3] venv`).
* En la línea de comandos, ejecutar `pip install -r requirements.txt`.
* Ejecutar `python servicio/api.py` y el servicio estará disponible en `http://localhost:5151/`

> Nótese que si se tiene instalado Python2 y Python3 simultáneamente (como en sistemas Linux), el comando `python` se reemplaza por `python3` y `pip` por `pip3`.

## Cliente web

[![Build Status](https://api.travis-ci.com/Dymmon/grafos-punto-jota-pe-ge.svg)](https://api.travis-ci.com/Dymmon/grafos-punto-jota-pe-ge.svg)

### Requerimientos

- Navegador web como [Firefox](https://www.mozilla.org/es-CL/firefox/new/), [Chrome](https://www.google.com/intl/es-419/chrome/), [Edge](https://www.microsoft.com/en-us/edge), [Opera](https://www.opera.com/es) o [Safari](https://www.apple.com/cl/safari/).
- [Node.js](https://nodejs.org/es/download/), solo en caso de querer servir o construir el código.

> Navegadores como IE no se recomiendan, ya que tienen soporte parcial o nulo.

### Abrir sitio web

- Situarse en la carpeta `cliente/dist` con `cd cliente/dist`.
- Abrir el archivo `index.html` con su navegador web.

### Construir sitio web

> Si sólo desea visualizar el sitio web, debe seguir [estas instrucciones](#abrir-sitio-web).

- Situarse en la carpeta `cliente` con `cd cliente`.
- Ejecutar `npm install` para instalar las dependencias.
- Contrurir el sitio con `npm run build` que generará todos los archivos dentro de la carpeta `cliente/dist`.

### Servir la web en modo desarrollo

> Si sólo desea visualizar el sitio web, debe seguir [estas instrucciones](#abrir-sitio-web).

- Situarse en la carpeta `cliente` con `cd cliente`.
- Ejecutar `npm install` para instalar las dependencias.
- Ejecutar `npm run serve` que ejecturá un servidor local con la aplicación web.
