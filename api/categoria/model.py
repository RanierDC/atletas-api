from base.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float, DateTime
from datetime import datetime
from atleta.model import AtletaModel

class CategoriaModel(BaseModel):
    __tablename__ = 'categoria'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    atleta: Mapped['AtletaModel'] = relationship(back_populates='categoria')
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now())
