# Backend - TP Integrador React 3

Backend desarrollado con FastAPI, SQLModel y SQLite para el TP Integrador de Programación IV.

## Tecnologías utilizadas

- Python
- FastAPI
- SQLModel
- SQLAlchemy
- SQLite
- Uvicorn
- Python Dotenv

## Funcionalidades

### Categorías

El backend permite realizar las siguientes operaciones:

- Listar categorías.
- Buscar una categoría por ID.
- Crear una categoría.
- Actualizar una categoría.
- Eliminar una categoría.

### Productos

El backend permite realizar las siguientes operaciones:

- Listar productos.
- Buscar un producto por ID.
- Crear un producto.
- Actualizar un producto.
- Eliminar un producto.

### Producto - Categoría

Se implementó una relación muchos a muchos entre productos y categorías mediante la tabla intermedia `ProductoCategoria`.

Esta relación permite:

- Asociar una categoría a un producto.
- Listar las relaciones existentes.
- Eliminar una relación entre producto y categoría.
- Evitar relaciones duplicadas.

## Estructura principal

```text
Backend
├── app
│   ├── core
│   │   └── database.py
│   ├── categoria
│   │   ├── model.py
│   │   ├── router.py
│   │   ├── schema.py
│   │   └── service.py
│   ├── producto
│   │   ├── model.py
│   │   ├── router.py
│   │   ├── schema.py
│   │   └── service.py
│   └── main.py
├── .env
├── .gitignore
├── requirements.txt
├── requests.http
└── README.md
```

## Base de datos

Para el desarrollo del proyecto se utiliza SQLite mediante SQLModel.

La configuración se encuentra en el archivo:

`app/core/database.py`

La dirección de conexión se configura mediante la variable `DATABASE_URL` del archivo `.env`.

## Instalación

Crear el entorno virtual:

```powershell
python -m venv .venv
```

Activar el entorno virtual en Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```powershell
pip install -r requirements.txt
```

## Ejecutar el backend

Con el entorno virtual activado, ejecutar:

```powershell
python -m uvicorn app.main:app --reload
```

El servidor estará disponible en:

`http://127.0.0.1:8000`

La documentación Swagger estará disponible en:

`http://127.0.0.1:8000/docs`

## Pruebas de endpoints

El archivo `requests.http` contiene las peticiones utilizadas para probar los endpoints mediante la extensión REST Client de Visual Studio Code.

Se incluyen pruebas para:

- Categorías.
- Productos.
- Relaciones entre productos y categorías.
- Validación de relaciones duplicadas.

## CORS

El backend tiene configurado CORS para permitir las solicitudes realizadas desde el frontend ejecutado en:

`http://localhost:5173`

De esta manera, la aplicación React puede comunicarse correctamente con la API desarrollada en FastAPI.