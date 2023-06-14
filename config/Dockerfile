# Получить базовый образ
FROM python:3.11
# Установите переменные среды
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Установите рабочую директорию
WORKDIR /code
# Установите зависимости
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system
# Копирование проекта
COPY . /code/
