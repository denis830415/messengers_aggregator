[app]

# Название приложения
title = MessengerAggregator

# Имя пакета (уникально!)
package.name = messengeraggregator
package.domain = org.example

# Версия приложения
version = 0.1.0

# Исходники
source.dir = .
source.include_exts = py,kv

# Главный файл
entrypoint = app/main.py

# Python
requirements = python3,kivy,kivymd,pyjnius

# Минимальная версия Android
android.minapi = 21

# Целевая версия Android
android.api = 33

# Разрешения
android.permissions = INTERNET,FOREGROUND_SERVICE,BIND_NOTIFICATION_LISTENER_SERVICE

# Архитектуры
android.archs = arm64-v8a,armeabi-v7a

# Сервисы (Java)
android.add_java_src = java

# Иконка (позже)
# icon.filename = app/ui/icon.png

# Ориентация экрана
orientation = portrait

# Логирование
log_level = 2

# Режим отладки
fullscreen = 0

[buildozer]

log_level = 2
warn_on_root = 1
