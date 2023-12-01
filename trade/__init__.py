from pydantic import BaseModel


class PublicTradeValidator(BaseModel):
    user_id: int
    trade_name: str
    category: str
    trade_text: str
    cost: int


class EditTradeValidator(BaseModel):
    user_id: int
    trade_name: str
    category: str
    new_text: str
    cost: int

