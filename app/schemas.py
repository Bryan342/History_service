from pydantic import BaseModel
from datetime import datetime

class TransactionCreate(BaseModel):
    idempotencyKey: str
    sender_wallet: str
    receiver_wallet: str
    amount: float
    currency: str
    timestamp: datetime