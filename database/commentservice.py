from .models import Comment

from datetime import datetime

from database import get_db


# Добавить коментарий
def add_comment_db(user_id, comment_text, trade_id):
    db = next(get_db())

    new_comment = Comment(trade_id=trade_id, comment_text=comment_text, user_id=user_id)

    db.add(new_comment)
    db.commit()

    return "Successfully added comment"


# Изменения определенный коментарий
def edit_comment_db(comment_id, new_comment):
    db = next(get_db())

    edit_comment = db.query(Comment).filter_by(id=comment_id).first()

    if edit_comment:
        edit_comment.comment_text = new_comment
        db.commit()

        return 'Successfully edited'
    else:
        return False


# Удаление коментарий
def delete_comment_db(comment_id):
    db = next(get_db())

    delete_comment = db.query(Comment).filter_by(id=comment_id).first()

    if delete_comment:
        db.delete(delete_comment)
        db.commit()

        return "Successfully deleted"
    else:
        return False


# Получить все коментарий определенного поста
def get_trade_comments(trade_id):
    db = next(get_db())

    trade_comment = db.query(Comment).filter_by(trade_id=trade_id).first()
    return trade_comment
