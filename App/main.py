from fastapi import FastAPI

app = FastAPI(title="Mi API - Demo CI/CD")

@app.get("/")
def read_root():
    return {"mensaje": "API funcionando correctamente"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/usuarios")
def get_usuarios():
    return {
        "usuarios": [
            {"id": 1, "nombre": "Ana"},
            {"id": 2, "nombre": "Luis"}
        ]
    }