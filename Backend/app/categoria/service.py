from sqlmodel import Session, select

from app.categoria.model import Categoria
from app.categoria.schema import CategoriaCreate, CategoriaUpdate


def obtener_categorias(session: Session):
    statement = select(Categoria)
    return session.exec(statement).all()


def obtener_categoria_por_id(categoria_id: int, session: Session):
    return session.get(Categoria, categoria_id)


def crear_categoria(datos: CategoriaCreate, session: Session):
    categoria = Categoria.model_validate(datos)

    session.add(categoria)
    session.commit()
    session.refresh(categoria)

    return categoria


def actualizar_categoria(
    categoria_id: int,
    datos: CategoriaUpdate,
    session: Session,
):
    categoria = session.get(Categoria, categoria_id)

    if categoria is None:
        return None

    nuevos_datos = datos.model_dump()

    for campo, valor in nuevos_datos.items():
        setattr(categoria, campo, valor)

    session.add(categoria)
    session.commit()
    session.refresh(categoria)

    return categoria


def eliminar_categoria(categoria_id: int, session: Session):
    categoria = session.get(Categoria, categoria_id)

    if categoria is None:
        return False

    session.delete(categoria)
    session.commit()

    return True