from .main import app  # Expone la instancia de FastAPI para importaciones fáciles
__all__ = ["app"]      # Define qué símbolos se exportan al usar `from api import *`