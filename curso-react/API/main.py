from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from models import Cadastros
from database import engine, Base, get_db
from repositories import CadastroRepository
from schemas import CadastroRequest, CadastroResponse
from middleware import add_cors_middleware

Base.metadata.create_all(bind=engine)
app = FastAPI()

add_cors_middleware(app)

@app.post("/api/cadastros/", response_model=CadastroResponse, status_code=status.HTTP_201_CREATED)
def create(email: str, nome: str, senha: str, db: Session = Depends(get_db)):
    cadastro = CadastroRepository.save(db, Cadastros(email=email, nome=nome, senha=senha))
    return CadastroResponse.from_orm(cadastro)

@app.get("/api/cadastros/", response_model=list[CadastroResponse])
def find_all(db: Session = Depends(get_db)):
    cadastros = CadastroRepository.find_all(db)
    return [CadastroResponse.from_orm(Cadastro) for Cadastro in cadastros]

@app.get("/api/cadastros/{id}", response_model=CadastroResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    cadastro = CadastroRepository.find_by_id(db, id)
    if not cadastro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cadastro não encontrado"
        )
    return CadastroResponse.from_orm(cadastro)

@app.delete("/api/cadastros/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not CadastroRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cadastro não encontrado"
        )
    CadastroRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/api/cadastros/{id}", response_model=CadastroResponse)
def update(id: int, request: CadastroRequest, db: Session = Depends(get_db)):
    if not CadastroRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cadastro não encontrado"
        )
    cadastro = CadastroRepository.save(db, Cadastros(id=id, **request.dict()))
    return CadastroResponse.from_orm(cadastro)