# FastAPI & Aiogram Telegram bot start template

This is a basic template for creating a Telegram bot using the [FastAPI](https://github.com/tiangolo/fastapi) framework and the [Aiogram](https://github.com/aiogram/aiogram) library in Python. It's a starting point for building your own Telegram bot with minimal setup.

## Prerequisites

- Python 3.10+
- Aiogram 3.0+
- FastAPI 0.100+
- redis

#### Description

Setup you own environment variables in settings.py file or in `[prod|dev].env` file. Put your own handlers in handlers directory and import them in __init__.py file. In REDIS saved ppid for checking if bot is running first time or not. But also you cat use it for cache or other purposes.