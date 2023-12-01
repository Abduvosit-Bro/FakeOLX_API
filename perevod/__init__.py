from pydantic import BaseModel


class CreateTransferValidator(BaseModel):
    card_from: int
    card_to: int
    amount: float

