from .models import UserTrade, TradePhoto
from datetime import datetime

from database import get_db



def add_trade_db(user_id, trade_text, cost, trade_name, category):
    db = next(get_db())

    new_trade = UserTrade(user_id=user_id,
                        trade_text=trade_text,
                        trade_name=trade_name,
                        category=category,
                        cost=cost,
                        publish_date=datetime.now())
    db.add(new_trade)
    db.commit()

    return 'Успешно добавлен'



def add_trade_photo_db(trade_id, trade_photo):
    db = next(get_db())

    new_trade_photo = TradePhoto(trade_id=trade_id, trade_photo=trade_photo)

    db.add(new_trade_photo)
    db.commit()

    return 'Фотография загружен'


def get_trade_photo_db():
    db = next(get_db())

    new_trade_photo = db.query(TradePhoto).all()

    return new_trade_photo


def edit_trade_db(trade_id, user_id, new_text):
    db = next(get_db())

    exact_trade = db.query(UserTrade).filter_by(id=trade_id, user_id=user_id).first()

    if exact_trade:
        exact_trade.trade_text = new_text
        db.commit()

        return 'Успешно изменено'
    else:
        return False



def delete_trade_db(trade_id):
    db = next(get_db())

    delete_trade = db.query(UserTrade).filter_by(id=trade_id).first()
    delete_trade_photo = db.query(TradePhoto).filter_by(trade_id=trade_id).first()

    if delete_trade:
        db.delete(*delete_trade_photo)
        db.commit()

        db.delete(delete_trade)
        db.commit()

        return "Успешно удалено"
    else:
        return False


def get_all_trades_db():
    db = next(get_db())

    all_trades = db.query(UserTrade).all()
    return all_trades

def get_exact_trade_db(trade_id):
    db = next(get_db())

    exact_trade = db.query(TradePhoto).filter_by(id=trade_id).first()

    if exact_trade:
        return exact_trade
    else:
        return 'Error'
