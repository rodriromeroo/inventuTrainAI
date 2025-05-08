from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from services.data_processor import procesar_csv
from core.analysis import entrenar_modelo, predecir_anomalias
from core.nlp import NLPProcessor
from database.crud import guardar_fallo
from database.session import SessionLocal
from .schemas import Consulta, CSVInput
import tempfile

app = FastAPI()
nlp_processor = NLPProcessor()

@app.post("/analizar")
async def analizar_locomotora(
    locomotora_id: str,
    consulta: str,
    csv_file: UploadFile = File(...),
    formato_csv: str = "filas"
):
    try:
        # 1. Procesar CSV
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(await csv_file.read())
            df = procesar_csv(tmp.name, formato_csv)

        # 2. Entrenar modelo y detectar anomalías (ejemplo con "valor" como variable)
        model = entrenar_modelo(df, variables=["valor"])
        anomalias = predecir_anomalias(model, df, variables=["valor"])

        # 3. Procesar consulta con NLP
        tipo_fallo = nlp_processor.clasificar_consulta(consulta)
        respuesta = nlp_processor.generar_respuesta(
            contexto=anomalias.to_string(),
            pregunta=consulta
        )

        # 4. Guardar en BD
        db = SessionLocal()
        guardar_fallo(db, locomotora_id, tipo_fallo, respuesta, 0.9)  # Probabilidad de ejemplo
        db.close()

        return JSONResponse(content={
            "respuesta": respuesta,
            "anomalias": anomalias.to_dict(orient="records")
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))