from fastapi import APIRouter, UploadFile
import os
photo_router = APIRouter(prefix='/photo', tags=['Фотографии'])



@photo_router.post('/add-photo')
async def add_user_profile_photo(photo_file: UploadFile, user_id: int):
    with open(f'media/{photo_file.filename}', 'wb') as file:
        user_photo = await photo_file.read()

        file.write(user_photo)

    return {'message': 'Successfully'}


@photo_router.put('/edit-photo')
async def edit_user_profile_photo(new_photo_file: UploadFile, user_id: int):
    with open(f'media/{new_photo_file.filename}', 'wb') as file:
        user_photo = await new_photo_file.read()

        file.write(user_photo)

    return {'message': 'Successfully edited'}


@photo_router.delete('/delete-photo')
async def delete_user_profile_photo(user_id: int):
    file_name = (user_id)

    if file_name is None:
        return {'message': 'Фото пользователя не найдено'}

    file_path = f'media/{file_name}'

    if os.path.exists(file_path):
        os.remove(file_path)
        return {'message': 'Фото успешно удалено'}
    else:
        return {'message': 'Файл не найден'}
