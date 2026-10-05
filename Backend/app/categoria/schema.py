from sqlmodel import SQLModel


class CategoriaBase(SQLModel):
    nombre: str
    descripcion: str


class CategoriaCreate(CategoriaBase):
    pass


class CategoriaUpdate(CategoriaBase):
    pass


class CategoriaRead(CategoriaBase):
    id: int