from fastapi import APIRouter, UploadFile, Body

from trade import PublicTradeValidator, EditTradeValidator

from database.tradeservice import add_trade_db, add_trade_photo_db, edit_trade_db, delete_trade_db, get_all_trades_db, \
    get_exact_trade_db

trade_router = APIRouter(prefix='/user_trade', tags=['Работа со сделками'])


# Запрос на публикации поста
@trade_router.post('/public_trade')
async def public_trade(data: PublicTradeValidator):
    result = add_trade_db(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message': 'Error'}


# Запрос для добавления фото к посту
@trade_router.post('/add_photo')
async def add_photo(trade_id: int = Body(),
                    user_id: int = Body(),
                    photo_file: UploadFile = None
                    ):
    photo_path = f'/media/{photo_file.filename}'
    try:
        # Сохранения фотографии в папку media
        with open(f'media/{photo_file.filename}', 'wb') as file:
            user_photo = await photo_file.read()

            file.write(user_photo)

        # Сохранения ссылки к фотографии в базу
        result = add_trade_photo_db(trade_id=trade_id, trade_photo=photo_path)

    except Exception as error:
        result = error

    return {'message': result}


# Запрос на изменения текста в публикации
@trade_router.put('/change_trade')
async def change_trade(data: EditTradeValidator):
    result = edit_trade_db(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message': 'Trade not found'}


# Запрос на удаления публикации
@trade_router.delete('/delete_trade')
async def delete_trade(trade_id: int):
    result = delete_trade_db(trade_id)

    if result:
        return {'message': result, 'status': 'Deleted'}
    else:
        return {'message': 'Trade not found'}


# Запрос на получения всех публикаций
@trade_router.get('/get_all_trades')
async def get_all_trades():
    result = get_all_trades_db()

    return {'message': result}


# Получить определенный пост
@trade_router.get('/get_exact_trade')
async def get_exact_trade(trade_id: int):
    result = get_exact_trade_db(trade_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Trade not found'}
