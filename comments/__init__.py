from pydantic import BaseModel


# Валидатор для публикаций коммента
class CommentValidator(BaseModel):
    comment_text: str
    user_id: int
    trade_id: int


# Валидатор для изменения комента
class EditCommentValidator(BaseModel):
    new_text: str
    comment_id: int
