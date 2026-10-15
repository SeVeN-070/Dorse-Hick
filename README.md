# [Dorse Hick]

Somos un equipo de desarrollo dedicado a crear soluciones de software eficientes y automatizar tareas claves para responder a las necesidades operativas de nuestros clientes.

## 👥 Integrantes del Equipo

| Nombre | Usuario de GitHub | Rol en la Empresa |
| Matías Bedoya | [@Matt-NotLab](https://github.com/Matt-NotLab) | Desarrollador |
| [Julian Jaramillo] | [@SeVeN-070](https://github.com/SeVeN-070) | Desarrollador |
| [Jose Manuel Giraldo] | [@jggm1528-cpu](https://github.com/jggm1528-cpu) | Desarrollador |
| [Dylan Mosquera] | [@gambinol](https://github.com/gambinol) | Desarrollador |
---

## 📁 Estructura del Repositorio

El proyecto está organizado según las siguientes carpetas y archivos clave:

* **`src/`**: Directorio donde vive el código fuente de las automatizaciones y funcionalidades del proyecto.
* **`docs/`**: Documentación técnica detallada y archivos adicionales que complementan el proyecto.
* **`equipo/`**: Perfiles profesionales e información de cada uno de los integrantes.
* **`README.md`**: Portada y descripción general del proyecto y la empresa.
* **`CONTRIBUTING.md`**: Guía y reglas de trabajo colaborativo para el flujo de Git y GitHub.
* **`.gitignore`**: Lista de archivos y carpetas que se excluyen del control de versiones (archivos temporales, entornos virtuales, credenciales, etc.).

## Estructura del Proyecto

* `generar_pedidos.py`: Script proporcionado para simular la recepción de archivos en la bandeja de entrada.
* `organizar.py`: Script principal de procesamiento y clasificación de pedidos.
* `sedes.py`: Módulo para la validación y normalización de las sedes (Itagüí, Envigado, Sabaneta, Bello).
* `lectores.py`: Módulo encargado de procesar los diferentes formatos de archivo (`.txt`, `.csv`, `.json`).
* `config.json`: Archivo de configuración general.
* `.gitignore`: Filtro para ignorar archivos temporales y carpetas de datos generadas.

## Requisitos Previos

* **Python 3.8** o superior instalado en el sistema.
* Entorno de consola (**Git Bash** o terminal integrada de VS Code).

## Instrucciones de Ejecución

### 1. Generar la bandeja de entrada de pedidos

Para simular la llegada de archivos de pedidos en la carpeta `bandeja_entrada/`, ejecuta el script según el lote deseado:

- **Lote 1 (Septiembre):**

Lote 1 (Septiembre):
python generar_pedidos.py

Lote 2 (Octubre):
python generar_pedidos.py --lote 2

Nota: La carpeta bandeja_entrada/ se creará automáticamente y no se rastreará en Git gracias al archivo .gitignore.

### 2. Procesar y organizar los pedidos
Una vez generados los pedidos en la bandeja de entrada, ejecuta el script principal para procesar, filtrar y mover los archivos válidos y dañados:

python organizar.py