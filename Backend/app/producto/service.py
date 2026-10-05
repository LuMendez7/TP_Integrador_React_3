from sqlmodel import Session, select

from app.categoria.model import Categoria, ProductoCategoria
from app.producto.model import Producto
from app.producto.schema import ProductoCreate, ProductoUpdate


def obtener_productos(session: Session):
    statement = select(Producto)
    return session.exec(statement).all()


def obtener_producto_por_id(producto_id: int, session: Session):
    return session.get(Producto, producto_id)


def crear_producto(datos: ProductoCreate, session: Session):
    producto = Producto.model_validate(datos)

    session.add(producto)
    session.commit()
    session.refresh(producto)

    return producto


def actualizar_producto(
    producto_id: int,
    datos: ProductoUpdate,
    session: Session,
):
    producto = session.get(Producto, producto_id)

    if producto is None:
        return None

    nuevos_datos = datos.model_dump()

    for campo, valor in nuevos_datos.items():
        setattr(producto, campo, valor)

    session.add(producto)
    session.commit()
    session.refresh(producto)

    return producto


def eliminar_producto(producto_id: int, session: Session):
    producto = session.get(Producto, producto_id)

    if producto is None:
        return False

    session.delete(producto)
    session.commit()

    return True


def asociar_categoria(
    producto_id: int,
    categoria_id: int,
    session: Session,
):
    producto = session.get(Producto, producto_id)
    categoria = session.get(Categoria, categoria_id)

    if producto is None or categoria is None:
        return None

    statement = select(ProductoCategoria).where(
        ProductoCategoria.producto_id == producto_id,
        ProductoCategoria.categoria_id == categoria_id,
    )

    relacion_existente = session.exec(statement).first()

    if relacion_existente:
        return False

    relacion = ProductoCategoria(
        producto_id=producto_id,
        categoria_id=categoria_id,
    )

    session.add(relacion)
    session.commit()

    return relacion

def obtener_relaciones(session: Session):
    statement = select(ProductoCategoria)
    return session.exec(statement).all()


def eliminar_relacion(
    producto_id: int,
    categoria_id: int,
    session: Session,
):
    statement = select(ProductoCategoria).where(
        ProductoCategoria.producto_id == producto_id,
        ProductoCategoria.categoria_id == categoria_id,
    )

    relacion = session.exec(statement).first()

    if relacion is None:
        return False

    session.delete(relacion)
    session.commit()

    return True