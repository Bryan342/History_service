from app.database import SessionLocal
from app.models import Transaction
from app.schemas import TransactionCreate

db = SessionLocal()

def create_transaction(tx: TransactionCreate):
    existing = db.query(Transaction).filter(Transaction.transaction_id == tx.transaction_id).first()
    if existing:
        return {"error": f"El transaction_id '{tx.transaction_id}' ya existe."}

    db_tx = Transaction(**tx.dict())
    try:
        db.add(db_tx)
        db.commit()
        db.refresh(db_tx)
        return db_tx
    except Exception as e:
        db.rollback()
        return {"error": f"Error al registrar la transacción: {str(e)}"}

def get_all_transactions():
    return db.query(Transaction).all()

def get_user_transactions(user_id: str):
    return db.query(Transaction).filter(Transaction.user_id == user_id).all()