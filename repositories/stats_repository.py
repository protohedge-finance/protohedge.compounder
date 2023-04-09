import json
from redis import Redis
from datetime import datetime


class StatsRepository:
    def __init__(self, redis: Redis):
        self.redis: Redis = redis

    def add_note(self, address: str, note: str):
        timestamp = int(datetime.now().timestamp() * 1000)
        record = "{}:{}:{}" .format((address.lower()), timestamp, note)
        self.redis.zadd("vault_notes", {record: 0})
        print("Added vault note {}".format(note))
