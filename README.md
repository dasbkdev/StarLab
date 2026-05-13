# Task Manager REST API

Современный Django-проект для управления задачами с:

- JWT авторизацией
- регистрацией пользователей
- CRUD задач
- фильтрацией по статусу
- pagination
- HTML интерфейсом
- красивой админкой на Jazzmin
- REST API на Django REST Framework

---

# Стек проекта

- Python 3.12+
- Django
- Django REST Framework
- SimpleJWT
- Django Filter
- Jazzmin
- SQLite

---

# Возможности

## Пользователи

- регистрация
- авторизация
- выход из системы
- JWT authentication

## Задачи

Каждый пользователь может:

- создавать задачи
- редактировать задачи
- удалять задачи
- просматривать свои задачи
- фильтровать задачи по статусу

## Статусы задач

```text
todo
in_progress
done

---

# Запуск проекта

## 1. Перейти в папку проекта

```bash
cd task-manager
```

## 2. Создать виртуальное окружение

```bash
python -m venv venv
```

## 3. Активировать виртуальное окружение

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## 4. Установить зависимости

```bash
pip install -r requirements.txt
```

## 5. Выполнить миграции

```bash
python manage.py makemigrations
python manage.py migrate
```

## 6. Создать администратора

```bash
python manage.py createsuperuser
```

## 7. Запустить сервер

```bash
python manage.py runserver
```

## 8. Открыть проект в браузере

Основной сайт:

```text
http://127.0.0.1:8000/
```

Админ-панель:

```text
http://127.0.0.1:8000/admin/
```

REST API:

```text
http://127.0.0.1:8000/api/tasks/
```