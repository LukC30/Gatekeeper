from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    __tablename__ = "tbl_usuario"

    id: Optional[int] = Field(None, primary_key=True)
    email: str = Field(None, unique=True, nullable=False)
    senha: str = Field(None, nullable=False)

    