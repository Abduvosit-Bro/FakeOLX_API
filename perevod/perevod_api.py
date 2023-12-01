from fastapi import APIRouter

from datetime import datetime

from database.perevodservice import create_transaction_db

from perevod import CreateTransferValidator

perevod_router = APIRouter(prefix='/transaction', tags=['Работа с платежами'])


# Запрос на создания транзакций
@perevod_router.post('/create')
async def add_new_transaction(data: CreateTransferValidator):
    transaction_data = data.model_dump()
    result = create_transaction_db(**transaction_data)

    return {'message': result}