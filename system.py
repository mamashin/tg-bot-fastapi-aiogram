# -*- coding: utf-8 -*-
__author__ = 'Nikolay Mamashin (mamashin@gmail.com)'

from os import getppid
import redis.asyncio as aredis
from settings import get_settings

cfg = get_settings()


async def first_run() -> bool:
    """Check if this is the first run of service. ppid is the parent process id.
    Save ppid to redis and check it on next run. If ppid is the same - this is not the first run."""
    ppid = getppid()
    redis = await aredis.from_url(cfg.redis_url)
    save_pid = await redis.get('tg_bot_ppid')
    if save_pid and int(save_pid) == ppid:
        await redis.close()
        return False
    await redis.set('tg_bot_ppid', ppid)
    await redis.close()
    return True
