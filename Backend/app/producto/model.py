from typing import TYPE_CHECKING

from sqlalchemy import Column, JSON
from sqlmodel import Field, Relationship, SQLModel

from app.categoria.model import ProductoCategoria

if TYPE_CHECKING:
    from app.categoria.model import Categoria


class Producto(SQLModel, table=True):
    __tablename__ = "producto"

    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    descripcion: str
    precio_base: str
    imagen_url: list[str] = Field(
        default_factory=list,
        sa_column=Column(JSON),
    )
    disponible: bool = True

    categorias: list["Categoria"] = Relationship(
        back_populates="productos",
        link_model=ProductoCategoria,
    )