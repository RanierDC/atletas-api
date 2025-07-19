from pydantic import Field, PositiveFloat
from typing import Annotated
from base.schemas import BaseSchema

class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Centro de Treinamento', examples='CT Mooca', max_length=20)]
    endereco: Annotated[str,Field(description='Endereço do Centro de Treinamento', examples='Rua Jośe Bonifácio, 679', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietário do Centro de Treinamento', examples='João', max_length=30)]