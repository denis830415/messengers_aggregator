"""
Парсер уведомлений мессенджеров.

Поддерживаемые источники:
- Telegram
- WhatsApp
- Viber
"""

# TODO: импортировать константы package names

class MessageParser:
    """Парсинг системных уведомлений"""

    def parse(self, raw_notification):
        """
        Преобразует системное уведомление в унифицированный формат

        :return: dict с полями:
            - messenger
            - sender
            - text
            - timestamp
        """
        # TODO: определить мессенджер
        # TODO: извлечь имя отправителя
        # TODO: извлечь текст сообщения
        pass
