from typing import AnyStr

from redis import StrictRedis

from git_resume.config import config
from git_resume.models.cont import ONE_WEEk


class _RedisBaseModel:
    """Base Model to Redis cache"""

    # Prefixe of all model keys
    key_prefixe: str = ''

    # Key ttl
    ttl: int = 0

    def __init__(self, *args, **kwargs):
        self.client = StrictRedis(**config.redis_config)

    def __normalized_key(self, key: str) -> str:
        return self.key_prefixe.upper() + ':' + key.upper()

    def get(self, key: str):
        return self.client.get(self.__normalized_key(key)) or {}

    def set(self, key, value: AnyStr):
        self.client.set(self.__normalized_key(key), value, self.ttl)

    def delete(self, key: str):
        self.client.delete(self.__normalized_key(key))


class GitHubDocumentCache(_RedisBaseModel):
    key_prefixe = 'GITHUB_CACHE:DOCUMENTS'
    ttl = ONE_WEEk

    def __init__(self, *args, **kwargs):
        super().__init__()
