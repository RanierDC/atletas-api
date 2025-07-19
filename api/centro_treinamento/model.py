from api.base.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey
from datetime import datetime
from api.categoria.model import AtletaModel

class CentroTreinamentoModel(BaseModel):
    __tablename__ = 'centro_treinamento'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)

    nome: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    proprietario: Mapped[str] = mapped_column(String(30), nullable=False)

    atleta: Mapped['AtletaModel'] = relationship(back_populates='centro_treinamento')
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now())