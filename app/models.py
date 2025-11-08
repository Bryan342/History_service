from sqlalchemy import Column, String, Float, DateTime
from app.database import Base

class Transaction(Base):
    __tablename__ = "Transaction"

    transaction_id = Column(String(255), primary_key=True, index=True)
    user_id = Column(String(50), index=True)
    sender_wallet = Column(String(50))
    receiver_wallet = Column(String(50))
    amount = Column(Float)
    currency = Column(String(10))
    type = Column(String(20))
    description = Column(String(255))
    status = Column(String(20))
    timestamp = Column(DateTime)