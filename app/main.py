from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para registrar una transacción
@app.post("/history/record")
def record_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_transaction(db, transaction)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint para consultar historial por usuario
@app.get("/history/user/{user_id}")
def get_user_history(user_id: str, db: Session = Depends(get_db)):
    history = db.query(models.Transaction).filter(models.Transaction.user_id == user_id).order_by(models.Transaction.timestamp.desc()).all()
    if not history:
        raise HTTPException(status_code=404, detail="No se encontró historial para este usuario")
    return history

# Endpoint para consultar movimientos contables por monedero
@app.get("/ledger/wallet/{wallet_id}")
def get_wallet_ledger(wallet_id: str, db: Session = Depends(get_db)):
    ledger = db.query(models.Ledger).filter(models.Ledger.wallet_id == wallet_id).order_by(models.Ledger.timestamp.desc()).all()
    if not ledger:
        raise HTTPException(status_code=404, detail="No se encontró movimientos para este monedero")
    return ledger