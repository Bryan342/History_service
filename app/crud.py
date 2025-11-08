from sqlalchemy.orm import Session
from app.models import Transaction, Wallet, Ledger, AuditLog
from datetime import datetime
import uuid

def create_transaction(db: Session, tx):
    wallet = db.query(Wallet).filter(Wallet.wallet_id == tx.sender_wallet).first()
    if not wallet:
        raise Exception("Wallet no encontrado")

    user_id = wallet.user_id

    # Verificar idempotencia
    existing = db.query(Transaction).filter(Transaction.transaction_id == tx.idempotencyKey).first()
    if existing:
        return existing

    # Crear transacción
    db_transaction = Transaction(
        transaction_id=tx.idempotencyKey,
        user_id=user_id,
        sender_wallet=tx.sender_wallet,
        receiver_wallet=tx.receiver_wallet,
        amount=tx.amount,
        currency=tx.currency,
        status="completed",
        timestamp=tx.timestamp
    )
    db.add(db_transaction)

    # Crear entradas en Ledger
    entries = [
        Ledger(
            ledger_id=str(uuid.uuid4()),
            transaction_id=tx.idempotencyKey,
            wallet_id=tx.sender_wallet,
            amount=-tx.amount,
            type="debit",
            timestamp=tx.timestamp
        ),
        Ledger(
            ledger_id=str(uuid.uuid4()),
            transaction_id=tx.idempotencyKey,
            wallet_id=tx.receiver_wallet,
            amount=tx.amount,
            type="credit",
            timestamp=tx.timestamp
        )
    ]
    for entry in entries:
        db.add(entry)

    # Crear entrada en Audit_Log
    audit = AuditLog(
        audit_id=str(uuid.uuid4()),
        user_id=user_id,
        action="create_transaction",
        executed_at=datetime.utcnow(),
        details=f"Transacción {tx.idempotencyKey} registrada"
    )
    db.add(audit)

    db.commit()
    db.refresh(db_transaction)
    return db_transaction