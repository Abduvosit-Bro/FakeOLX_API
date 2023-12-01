from fastapi import FastAPI

from comments.comment_api import comment_router
from paycard.paycard_api import paycard_router
from perevod.perevod_api import perevod_router
from photo.photo_api import photo_router
from trade.user_trade_api import trade_router
from user.user_api import user_router
# Для запуска БД
from database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/")

app.include_router(user_router)
app.include_router(photo_router)
app.include_router(trade_router)
app.include_router(paycard_router)
app.include_router(perevod_router)
app.include_router(comment_router)

@app.get('/test')
async def test():
    return 'This is test page'
