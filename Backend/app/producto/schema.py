from sqlmodel import Field, SQLModel


class ProductoBase(SQLModel):
    nombre: str
    descripcion: str
    precio_base: str
    imagen_url: list[str] = Field(default_factory=list)
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

class ProductoCategoriaUpdate(SQLModel):
    nuevo_producto_id: int
    nueva_categoria_id: int