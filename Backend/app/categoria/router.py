from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlmodel import Session

from app.core.database import get_session
from app.categoria.schema import (
    CategoriaCreate,
    CategoriaRead,
    CategoriaUpdate,
)
from app.categoria.service import (
    actualizar_categoria,
    crear_categoria,
    eliminar_categoria,
    obtener_categoria_por_id,
    obtener_categorias,
)

router = APIRouter(
    prefix="/categorias",
    tags=["Categorias"],
)


@router.get("/", response_model=list[CategoriaRead])
def listar_categorias(
    session: Session = Depends(get_session),
):
    return obtener_categorias(session)


@router.get("/{categoria_id}", response_model=CategoriaRead)
def buscar_categoria(
    categoria_id: int = Path(gt=0),
    session: Session = Depends(get_session),
):
    categoria = obtener_categoria_por_id(categoria_id, session)

    if categoria is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoria no encontrada",
        )

    return categoria


@router.post(
    "/",
    response_model=CategoriaRead,
    status_code=status.HTTP_201_CREATED,
)
def agregar_categoria(
    datos: CategoriaCreate,
    session: Session = Depends(get_session),
):
    return crear_categoria(datos, session)


@router.put("/{categoria_id}", response_model=CategoriaRead)
def modificar_categoria(
    datos: CategoriaUpdate,
    categoria_id: int = Path(gt=0),
    session: Session = Depends(get_session),
):
    categoria = actualizar_categoria(categoria_id, datos, session)

    if categoria is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoria no encontrada",
        )

    return categoria


@router.delete(
    "/{categoria_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def borrar_categoria(
    categoria_id: int = Path(gt=0),
    session: Session = Depends(get_session),
):
    eliminado = eliminar_categoria(categoria_id, session)

    if not eliminado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoria no encontrada",
        )