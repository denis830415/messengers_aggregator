"""
Работа с Android NotificationListenerService.

Ответственность:
- Получение уведомлений из Java-сервиса
- Передача данных в Python-часть приложения
"""

# TODO: импортировать pyjnius
# TODO: подключить Java NotificationListener

class NotificationService:
    """Сервис приема уведомлений"""

    def start(self):
        """Запуск сервиса"""
        # TODO: инициализация Android сервиса
        pass

    def on_notification_received(self, raw_notification):
        """
        Обработка нового уведомления

        :param raw_notification: данные из Android
        """
        # TODO: передать уведомление в parser
        pass
