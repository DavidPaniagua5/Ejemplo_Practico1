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

@app.get("/usuarios/{usuario_id}")
def get_usuario_por_id(usuario_id: int):
    usuarios = {
        1: {"id": 1, "nombre": "Ana"},
        2: {"id": 2, "nombre": "Luis"}
    }
    if usuario_id in usuarios:
        return usuarios[usuario_id]
    return {"error": "Usuario no encontrado"}