from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlmodel import Session

from app.core.database import get_session
from app.producto.schema import (
    ProductoCategoriaCreate,
    ProductoCategoriaUpdate,
    ProductoCreate,
    ProductoRead,
    ProductoUpdate,
)
from app.producto.service import (
    actualizar_producto,
    actualizar_relacion,
    asociar_categoria,
    crear_producto,
    eliminar_producto,
    eliminar_relacion,
    obtener_producto_por_id,
    obtener_productos,
    obtener_relaciones,
)

router = APIRouter(
    prefix="/productos",
    tags=["Productos"],
)


@router.get("/", response_model=list[ProductoRead])
def listar_productos(
    session: Session = Depends(get_session),
):
    return obtener_productos(session)


@router.get("/{producto_id}", response_model=ProductoRead)
def buscar_producto(
    producto_id: int = Path(gt=0),
    session: Session = Depends(get_session),
):
    producto = obtener_producto_por_id(producto_id, session)

    if producto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado",
        )

    return producto


@router.post(
    "/",
    response_model=ProductoRead,
    status_code=status.HTTP_201_CREATED,
)
def agregar_producto(
    datos: ProductoCreate,
    session: Session = Depends(get_session),
):
    return crear_producto(datos, session)


@router.put("/{producto_id}", response_model=ProductoRead)
def modificar_producto(
    datos: ProductoUpdate,
    producto_id: int = Path(gt=0),
    session: Session = Depends(get_session),
):
    producto = actualizar_producto(producto_id, datos, session)

    if producto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado",
        )

    return producto


@router.delete(
    "/{producto_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def borrar_producto(
    producto_id: int = Path(gt=0),
    session: Session = Depends(get_session),
):
    eliminado = eliminar_producto(producto_id, session)

    if not eliminado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado",
        )


@router.post(
    "/categorias/asociar",
    status_code=status.HTTP_201_CREATED,
)
def agregar_categoria_a_producto(
    datos: ProductoCategoriaCreate,
    session: Session = Depends(get_session),
):
    resultado = asociar_categoria(
        datos.producto_id,
        datos.categoria_id,
        session,
    )

    if resultado is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto o categoria no encontrado",
        )

    if resultado is False:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="La relacion ya existe",
        )

    return {"mensaje": "Categoria asociada correctamente al producto"}

@router.get("/categorias/relaciones")
def listar_relaciones(
    session: Session = Depends(get_session),
):
    return obtener_relaciones(session)


@router.delete(
    "/categorias/{producto_id}/{categoria_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def quitar_categoria_de_producto(
    producto_id: int = Path(gt=0),
    categoria_id: int = Path(gt=0),
    session: Session = Depends(get_session),
):
    eliminado = eliminar_relacion(
        producto_id,
        categoria_id,
        session,
    )

    if not eliminado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Relacion no encontrada",
        )

@router.put("/categorias/{producto_id}/{categoria_id}")
def modificar_relacion(
    datos: ProductoCategoriaUpdate,
    producto_id: int = Path(gt=0),
    categoria_id: int = Path(gt=0),
    session: Session = Depends(get_session),
):
    resultado = actualizar_relacion(
        producto_id,
        categoria_id,
        datos.nuevo_producto_id,
        datos.nueva_categoria_id,
        session,
    )

    if resultado == "relacion_no_encontrada":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Relacion Producto-Categoria no encontrada",
        )

    if resultado == "recurso_no_encontrado":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto o categoria no encontrado",
        )

    if resultado == "relacion_duplicada":
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="La relacion Producto-Categoria ya existe",
        )

    return resultado