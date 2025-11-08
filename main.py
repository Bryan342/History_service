from fastapi import FastAPI
from app import models
from app.database import engine
from app.crud import create_transaction, get_all_transactions, get_user_transactions
from app.schemas import TransactionCreate

# Crear las tablas en la base de datos
models.Base.metadata.create_all(bind=engine)

# Inicializar la aplicación FastAPI
app = FastAPI()

# Endpoint raíz
@app.get("/")
def read_root():
    return {"message": "Microservicio activo"}

# Endpoint para registrar una transacción
@app.post("/history/record")
def record_transaction(tx: TransactionCreate):
    return create_transaction(tx)

# Endpoint para obtener todas las transacciones
@app.get("/history")
def read_all():
    return get_all_transactions()

# Endpoint para obtener transacciones por usuario
@app.get("/history/{user_id}")
def read_user_history(user_id: str):
    return get_user_transactions(user_id)