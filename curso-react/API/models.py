from sqlalchemy import Column, Integer, String

from database import Base

class Cadastros(Base):
    __tablename__ = "cadastros"

    id: int = Column(Integer, primary_key=True, index=True)
    email: str = Column(String(100), nullable=False)
    nome: str = Column(String(255), nullable=False)
    senha: str = Column(String(100), nullable=False)
