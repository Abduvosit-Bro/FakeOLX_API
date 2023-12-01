from pydantic import BaseModel

# Валидатор пуции п_nameоста
class PublicTradeValidator(BaseModel):
    user_id: int
    trade_name: str
    category: str
    trade_text: str
    cost: int

# Валидатор для изменения текста к посту
class EditTradeValidator(BaseModel):
    user_id: int
    trade_name: str
    category: str
    new_text: str
    cost: int

