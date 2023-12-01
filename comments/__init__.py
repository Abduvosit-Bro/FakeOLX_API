from pydantic import BaseModel



class CommentValidator(BaseModel):
    comment_text: str
    user_id: int
    trade_id: int



class EditCommentValidator(BaseModel):
    new_text: str
    comment_id: int
