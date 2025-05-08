from sqlalchemy.orm import Session
from .models import Fallo
from .session import SessionLocal

def guardar_fallo(db: Session, locomotora_id: str, tipo: str, descripcion: str, probabilidad: float):
    db_fallo = Fallo(
        locomotora_id=locomotora_id,
        tipo=tipo,
        descripcion=descripcion,
        probabilidad=probabilidad
    )
    db.add(db_fallo)
    db.commit()
    db.refresh(db_fallo)
    return db_fallo