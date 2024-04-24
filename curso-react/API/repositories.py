from sqlalchemy.orm import Session

from models import Cadastros

class CadastroRepository:
    @staticmethod
    def find_all(db: Session) -> list[Cadastros]:
        return db.query(Cadastros).all()

    @staticmethod
    def save(db: Session, cadastro: Cadastros) -> Cadastros:
        if cadastro.id:
            db.merge(cadastro)
        else:
            db.add(cadastro)
        db.commit()
        return cadastro

    @staticmethod
    def find_by_id(db: Session, id: int) -> Cadastros:
        return db.query(Cadastros).filter(Cadastros.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Cadastros).filter(Cadastros.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        cadastro = db.query(Cadastros).filter(Cadastros.id == id).first()
        if cadastro is not None:
            db.delete(cadastro)
            db.commit()
