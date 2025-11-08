from pydantic import BaseModel
from datetime import datetime

class TransactionCreate(BaseModel):
    transaction_id: str
    user_id: str
    sender_wallet: str
    receiver_wallet: str
    amount: float
    currency: str
    type: str
    description: str
    status: str
    timestamp: datetime