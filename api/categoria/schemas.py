from pydantic import Field, PositiveFloat
from typing import Annotated
from base.schemas import BaseSchema

class Categoria(BaseSchema):
    nome: Annotated[str, Field(description='Nome da Categoria', examples='Natação', max_length=50)]
