from pydantic import BaseModel

class Consulta(BaseModel):
    texto: str

class CSVInput(BaseModel):
    locomotora_id: str
    formato_csv: str = "filas"