# Используем официальный python 3.10
FROM python:3.10

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем весь проект в контейнер
COPY . /app

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт
EXPOSE 8000

# Запускаем сервер
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
