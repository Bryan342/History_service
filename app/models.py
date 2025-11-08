from sqlalchemy import Column, String, Float, DateTime
from app.database import Base

class Wallet(Base):
    __tablename__ = "Wallet"
    wallet_id = Column(String(50), primary_key=True, index=True)
    user_id = Column(String(50), index=True)

class Transaction(Base):
    __tablename__ = "Transaction"
    transaction_id = Column(String(255), primary_key=True, index=True)
    user_id = Column(String(50), index=True)
    sender_wallet = Column(String(50))
    receiver_wallet = Column(String(50))
    amount = Column(Float)
    currency = Column(String(10))
    status = Column(String(20))
    timestamp = Column(DateTime)

class Ledger(Base):
    __tablename__ = "Ledger"
    ledger_id = Column(String(255), primary_key=True, index=True)
    transaction_id = Column(String(255), index=True)
    wallet_id = Column(String(50), index=True)
    amount = Column(Float)
    type = Column(String(20))
    timestamp = Column(DateTime)

class AuditLog(Base):
    __tablename__ = "Audit_Log"
    audit_id = Column(String(255), primary_key=True, index=True)
    user_id = Column(String(50), index=True)
    action = Column(String(50))
    executed_at = Column(DateTime)
    details = Column(String(255))