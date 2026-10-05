# Frontend - TP Integrador React 3

Frontend desarrollado con React, TypeScript, Vite y Tailwind CSS para el TP Integrador de Programación IV.

La aplicación se comunica con el backend desarrollado en FastAPI y permite realizar el CRUD completo de categorías desde una interfaz web.

## Tecnologías utilizadas

- React
- TypeScript
- Vite
- Tailwind CSS
- Fetch API

## Funcionalidades

La aplicación permite:

- Listar las categorías registradas.
- Crear nuevas categorías.
- Editar categorías existentes.
- Eliminar categorías.
- Utilizar un modal para crear y modificar categorías.
- Comunicarse con el backend mediante Fetch API.
- Actualizar automáticamente el listado luego de realizar una operación.
- Mostrar la información mediante componentes reutilizables.
- Utilizar estilos mediante Tailwind CSS.

## Componentes

La aplicación utiliza los siguientes componentes:

### Navbar

Componente encargado de mostrar la barra superior de la aplicación.

Archivo:

`src/components/Navbar.tsx`

### CategoriaCard

Muestra la información de cada categoría junto con los botones para editar y eliminar.

Archivo:

`src/components/CategoriaCard.tsx`

### CategoriaList

Recibe el listado de categorías y genera una tarjeta para cada una.

Archivo:

`src/components/CategoriaList.tsx`

### CategoriaModal

Modal utilizado para crear una nueva categoría o modificar una categoría existente.

Archivo:

`src/components/CategoriaModal.tsx`

## Tipos TypeScript

Se definieron interfaces TypeScript para trabajar con los datos de la aplicación.

Los archivos se encuentran en:

`src/types/categoria.ts`

`src/types/producto.ts`

Entre los tipos utilizados se encuentran:

- `Categoria`
- `CategoriaForm`
- `Producto`

## Comunicación con el backend

La aplicación utiliza la función nativa `fetch` para realizar las solicitudes HTTP al backend.

Se utilizan los siguientes métodos:

- GET para obtener las categorías.
- POST para crear categorías.
- PUT para modificar categorías.
- DELETE para eliminar categorías.

La API de categorías se encuentra en:

`http://127.0.0.1:8000/categorias`

## Estructura principal

```text
Frontend
├── src
│   ├── components
│   │   ├── Navbar.tsx
│   │   ├── CategoriaCard.tsx
│   │   ├── CategoriaList.tsx
│   │   └── CategoriaModal.tsx
│   ├── types
│   │   ├── categoria.ts
│   │   └── producto.ts
│   ├── App.tsx
│   ├── index.css
│   └── main.tsx
├── package.json
├── vite.config.ts
└── README.md
```

## Instalación

Instalar las dependencias:

```powershell
pnpm install
```

## Ejecutar el frontend

Ejecutar:

```powershell
pnpm dev
```

La aplicación estará disponible en:

`http://localhost:5173`

## Backend

Para utilizar correctamente todas las funcionalidades del frontend, el backend debe estar ejecutándose en:

`http://127.0.0.1:8000`

## Verificación

El proyecto fue verificado mediante:

```powershell
pnpm build
```

y:

```powershell
pnpm lint
```

Ambos comandos finalizaron sin errores.