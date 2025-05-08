from transformers import pipeline

class NLPProcessor:
    def __init__(self):
        self.classifier = pipeline(
            "text-classification", 
            model="distilbert-base-multilingual-cased"
        )
        self.generator = pipeline(
            "text-generation", 
            model="google-t5-small"
        )

    def clasificar_consulta(self, texto: str) -> str:
        return self.classifier(texto)[0]["label"]

    def generar_respuesta(self, contexto: str, pregunta: str) -> str:
        input_text = f"Pregunta: {pregunta} Contexto: {contexto}"
        return self.generator(input_text, max_length=200)[0]["generated_text"]