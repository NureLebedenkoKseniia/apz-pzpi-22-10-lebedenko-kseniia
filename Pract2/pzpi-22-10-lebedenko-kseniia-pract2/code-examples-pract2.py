#   Запит до інструменту штучного інтелекту (Gemini 3.1 Pro):
	
#	Напиши програмний скрипт мовою Python для демонстрації клієнт-серверної архітектури Docker. Скрипт повинен імітувати роботу клієнтського додатка. Необхідно реалізувати підключення до фонового процесу управління. Код має містити кроки завантаження образу із зовнішнього реєстру та запуск ізольованого контейнера. Також потрібно продемонструвати отримання статусу виконання через програмний інтерфейс.

import docker

client = docker.from_env()

image_name = "alpine:latest"
client.images.pull(image_name)

container = client.containers.run(
    image_name,
    command="echo Запуск процесу виконано успішно",
    detach=True
)

container.wait()

logs = container.logs().decode("utf-8")
print(logs)

#	Запит до інструменту штучного інтелекту (Gemini 3.1 Pro):

#	Створи декларативний конфігураційний файл для демонстрації принципу слабкого зв'язування та ізоляції. Налаштуй взаємодію веб-сервера з ізольованою базою даних. Передай параметри підключення через змінні середовища без використання жорстко закодованих мережевих адрес. Делегуй завдання маршрутизації вбудованому серверу доменних імен платформи. Додай механізм автоматичного перезапуску для обробки помилок.
version: '3.8'

services:
  web:
    image: nginx:latest
    ports:
      - "8080:80"
    environment:
      - DB_HOST=database
      - DB_PORT=5432
    depends_on:
      - database
    restart: always

  database:
    image: postgres:13
    environment:
      - POSTGRES_USER=admin
      - POSTGRES_PASSWORD=secret
      - POSTGRES_DB=app_db
    restart: on-failure

#	Запит до інструменту штучного інтелекту (Gemini 3.1 Pro):
	
#	Напиши конфігурації для демонстрації зберігання та дистрибуції даних у системі з шаруватою архітектурою. Розділи рівні доступу до файлової системи. Налаштуй ефемерні шари для тимчасових процесів виконання. Створи іменований том для постійного зберігання даних бази. Покажи делегування доставки контенту базових образів із зовнішніх реєстрів.

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]

###

version: '3.8'

services:
  app:
    build: .
    ports:
      - "5000:5000"

  db:
    image: redis:alpine
    volumes:
      - redis_data:/data

volumes:
  redis_data: