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