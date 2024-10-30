from telethon import TelegramClient
import os
import asyncio

# Установите ваши API_ID и API_HASH
api_id = '20614054'  # Замените на ваш API ID
api_hash = '6f43138161fb60b46083dc4740231d36'  # Замените на ваш API Hash

# Инициализация клиента Telethon
client = TelegramClient('session_name', api_id, api_hash)

async def get_channel_info(channel_username):
    await client.start()
    
    try:
        # Получаем информацию о канале
        channel = await client.get_entity(channel_username)
        
        # Получаем URL фотографии, если фото профиля есть
        photo_url = None
        if channel.photo:
            file = await client.download_profile_photo(channel, file=bytes)
            photo_url = f"data:image/jpeg;base64,{file.encode('base64').decode()}"
        
        # Получаем количество подписчиков, если доступно
        subscribers_count = channel.participants_count if hasattr(channel, 'participants_count') else "N/A"
        
        # Печать информации о канале
        print(f"Channel name: {channel.title}")
        print(f"Subscribers: {subscribers_count}")
        print(f"Photo URL: {photo_url}")
        
        return {
            "name": channel.title,
            "subscribers": subscribers_count,
            "photo_url": photo_url
        }
    except Exception as e:
        print(f"Error: {e}")
        return None

# Вызов функции для получения информации о канале
channel_username = '@reevnge'  # Укажите актуальное имя канала
channel_info = asyncio.run(get_channel_info(channel_username))
print(channel_info)  # Выводим информацию о канале
