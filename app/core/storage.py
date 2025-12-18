"""
Локальное хранилище сообщений (SQLite).

Ответственность:
- Сохранение истории
- Получение сообщений
- Очистка устаревших данных
"""

import sqlite3

class Storage:
    """SQLite-хранилище"""

    def __init__(self, db_path="messages.db"):
        # TODO: инициализация БД
        pass

    def save_message(self, message):
        """Сохранить сообщение"""
        # TODO: INSERT
        pass

    def get_messages(self, limit=100):
        """Получить список сообщений"""
        # TODO: SELECT
        pass

    def cleanup(self, days):
        """Удалить старые сообщения"""
        # TODO: DELETE по timestamp
        pass
