from fastapi import APIRouter

from comments import CommentValidator, EditCommentValidator

from database.commentservice import add_comment_db, edit_comment_db, delete_comment_db, get_trade_comments

comment_router = APIRouter(prefix='/comment', tags=['Работа с коментариями'])



@comment_router.post('/add_comment')
async def add_comment(data: CommentValidator):
    result = add_comment_db(data.user_id, data.comment_text, data.trade_id)
    if result:
        return {"message": result}
    return {"message": "Ошибка при добавлении комментария"}


@comment_router.put('/edit_comment')
async def edit_comment(data: EditCommentValidator):
    result = edit_comment_db(data.comment_id, data.new_comment)
    if result:
        return {"message": result}
    return {"message": "Комментарий не найден"}


@comment_router.delete('/delete_comment')
async def delete_comment(comment_id: int):
    result = delete_comment_db(comment_id)
    if result:
        return {"message": result}
    return {"message": "Комментарий не найден"}


@comment_router.get('/get_comments')
async def get_comments(trade_id: int):
    comments = get_trade_comments(trade_id)
    if comments:
        return comments
    return {"message": "Комментарии к посту не найдены"}
