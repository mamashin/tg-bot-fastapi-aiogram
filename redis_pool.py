# -*- coding: utf-8 -*-
__author__ = 'Nikolay Mamashin (mamashin@gmail.com)'

from redis.asyncio.connection import ConnectionPool

from settings import get_settings

cfg = get_settings()

pool = ConnectionPool.from_url(cfg.redis_url)
