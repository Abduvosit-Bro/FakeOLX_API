from fastapi import APIRouter
from paycard import CardInfoValidator
from database.paycardservice import add_card_db, check_card_db, delete_card_db

paycard_router = APIRouter(prefix='/card', tags=['Управление картами'])


@paycard_router.post('/add_new_card')
async def add_new_card(card: CardInfoValidator):
    if check_card_db(card.card_number):
        return {"message": "Карта уже существует"}

    result = add_card_db(card.user_id, card.card_number, card.expiration_date, card.cardholder_name, card.cvv)
    return result




@paycard_router.delete('/delete_card/{card_id}')
async def delete_card(card_id: int):
    result = delete_card_db(card_id)
    if result == 'Карта успешно удален':
        return {"message": result}
    return {"message": "Карта не найдена"}
