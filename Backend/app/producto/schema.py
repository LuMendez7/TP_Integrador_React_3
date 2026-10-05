from sqlmodel import SQLModel


class ProductoBase(SQLModel):
    nombre: str
    descripcion: str
    precio_base: str
    imagen_url: list[str] = []
    disponible: bool = True


class ProductoCreate(ProductoBase):
    pass


class ProductoUpdate(ProductoBase):
    pass


class ProductoRead(ProductoBase):
    id: int


class ProductoCategoriaCreate(SQLModel):
    producto_id: int
    categoria_id: int