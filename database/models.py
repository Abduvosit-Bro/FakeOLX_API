from sqlalchemy import Column, Float, String, Integer, Boolean, DateTime, ForeignKey

from sqlalchemy.orm import relationship

from database import Base


# Создаем таблицу пользователя
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    phone_number = Column(String)
    city = Column(String)
    profile_photo = Column(String)
    password = Column(String)
    reg_date = Column(DateTime)


# Таблица публикаций
class UserTrade(Base):
    __tablename__ = 'user_trades'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    trade_name = Column(String)
    category = Column(String)
    trade_text = Column(String)
    cost = Column(Integer, default=0)
    publish_date = Column(DateTime)

    user_fk = relationship(User, lazy="subquery")

# Таблица фотографий
class TradePhoto(Base):
    __tablename__ = 'trade_photos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    trade_id = Column(Integer, ForeignKey("user_trades.id"))
    trade_photo = Column(String)

    trade_fk = relationship(UserTrade, lazy='subquery')

# Таблица для комментарий
class Comment(Base):
    __tablename__ = 'trade_comments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    trade_id = Column(Integer, ForeignKey('user_trades.id'))
    comment_text = Column(String)

    user_fk = relationship(User, lazy='subquery')
    trade_fk = relationship(UserTrade, lazy='subquery')



# Таблица карт пользователя
class UserCard(Base):
    __tablename__ = 'cards'
    card_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    card_number = Column(String, nullable=False, unique=True)
    balance = Column(Float, default=0)
    exp_date = Column(DateTime, nullable=False)
    card_name = Column(String)

    user_fk = relationship(User, lazy='subquery')




# Таблица перевода - Transfers
class Transfer(Base):
    __tablename__ = 'transfers'
    transfer_id = Column(Integer, primary_key=True, autoincrement=True)
    card_from_id = Column(Integer, ForeignKey('cards.card_id'))
    card_to_id = Column(Integer, ForeignKey('cards.card_id'))
    amount = Column(Float)

    status = Column(Boolean, default=True)

    transaction_date = Column(DateTime)

    card_from_fk = relationship(UserCard, foreign_keys=[card_from_id], lazy='subquery')
    card_to_fk = relationship(UserCard, foreign_keys=[card_to_id], lazy='subquery')