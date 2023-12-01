from pydantic import BaseModel


class CardInfoValidator(BaseModel):
    card_number: str
    expiration_date: str
    cardholder_name: str
    cvv: str


class CardInfoResponseValidator(BaseModel):
    card_id: int
    user_id: int
    card_number: str
    expiration_date: str


class CardIDValidator(BaseModel):
    card_id: int


class UserIDValidator(BaseModel):
    user_id: int
