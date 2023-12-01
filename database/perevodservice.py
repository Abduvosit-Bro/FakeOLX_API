from datetime import datetime

from database.models import Transfer, UserCard
from database import get_db


# Проверка карты
def validate_card(card_number, db):
    exact_card = db.query(UserCard).filter_by(card_number=card_number).first()

    return exact_card


# Создания перевода
def create_transaction_db(card_from, card_to, amount):
    db = next(get_db())

    # Проверка на наличии карты в бд обеих карт
    check_card_from = validate_card(card_from, db)
    check_card_to = validate_card(card_to, db)

    # Если обе карты существуют в бд перевод
    if check_card_from and check_card_to:
        # Проверить баланс у отправителя
        if check_card_from.balance >= amount:
            # минусуем у того кто отправил
            check_card_from.balance -= amount
            # Добавляем тому кто получает
            check_card_to.balance += amount

            # Сохраняем платеж в бд
            new_transaction = Transfer(card_from_id=check_card_from.card_id,
                                       card_to_id=check_card_to.card_id,
                                       amount=amount,
                                       transaction_date=datetime.now()
                                       )
            db.add(new_transaction)
            db.commit()

            return "Перевод успешно выполнен"
        else:
            return "Недостаточно средств на балансе"
    else:
        return "Одна из карт не существует"


