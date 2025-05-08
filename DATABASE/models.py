from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Fallo(Base):
    __tablename__ = "fallos"
    id = Column(Integer, primary_key=True, index=True)
    locomotora_id = Column(String(50), nullable=False)
    tipo = Column(String(100))  # Ej: "eléctrico", "mecánico"
    descripcion = Column(String(500))
    probabilidad = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)