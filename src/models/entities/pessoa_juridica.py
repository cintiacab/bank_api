from sqlalchemy import Column, String, Float, BIGINT, ForeignKey
from src.models.settings.base import Base

class PessoaJuridicaTable(Base):
    __tablename__ = "pessoa_juridica"

    id = Column(BIGINT, primary_key=True)
    faturamento = Column(Float, nullable=False)
    idade = Column(BIGINT, nullable=False)
    nome_fantasia = Column(String, nullable=False)
    celular = Column(String, nullable=False)
    email_corporativo = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    saldo = Column(Float, nullable=False)
