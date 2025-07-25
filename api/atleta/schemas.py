from pydantic import Field, PositiveFloat
from typing import Annotated
from base.schemas import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', examples='Joao', max_length=50)]
    cpf: Annotated[str, Field(description='Cpf do atleta', examples='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', examples=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', examples=80.0)]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', examples=1.8)]
    sexo: Annotated[str, Field(description='Sexo do atleta', examples='M', max_length=1)]