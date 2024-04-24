from pydantic import BaseModel

class CadastroBase(BaseModel):
    email: str
    nome: str
    senha: str

class CadastroRequest(CadastroBase):
    email: str
    nome: str
    senha: str

class CadastroResponse(CadastroBase):
    id: int
    email: str
    nome: str

    class Config:
        from_attributes = True
