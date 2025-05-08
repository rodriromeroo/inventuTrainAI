from .session import engine, SessionLocal
from .models import Base, Fallo
from .crud import guardar_fallo
__all__ = ["engine", "SessionLocal", "Base", "Fallo", "guardar_fallo"]