import os


class Config:
    _REDIS_DEVELOPMENT_HOST = 'localhost'
    _REDIS_DEVELOPMENT_PORT = 6379
    _REDIS_DEVELOPMENT_USER = None
    _REDIS_DEVELOPMENT_PASSWORD = None

    REDIS_HOST = os.getenv('REDIS_HOST', _REDIS_DEVELOPMENT_HOST)
    REDIS_PORT = os.getenv('REDIS_PORT', _REDIS_DEVELOPMENT_PORT)
    REDIS_USER = os.getenv('REDIS_USER', _REDIS_DEVELOPMENT_USER)
    REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', _REDIS_DEVELOPMENT_PASSWORD)

    _RABBITMQ_DEVELOPMENT_HOST = '127.0.0.1'
    _RABBITMQ_DEVELOPMENT_PORT = 5672
    _RABBITMQ_DEVELOPMENT_USER = 'guest'
    _RABBITMQ_DEVELOPMENT_PASSWORD = 'guest'
    RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', _RABBITMQ_DEVELOPMENT_HOST)
    RABBITMQ_PORT = os.getenv('RABBITMQ_PORT', _RABBITMQ_DEVELOPMENT_PORT)
    RABBITMQ_USER = os.getenv('RABBITMQ_USER', _RABBITMQ_DEVELOPMENT_USER)
    RABBITMQ_PASSWORD = os.getenv(
        'RABBITMQ_PASSWORD', _RABBITMQ_DEVELOPMENT_PASSWORD
    )
    AMQP_URI = (
        f'amqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@'
        f'{RABBITMQ_HOST}:{RABBITMQ_PORT}'
    )
    print(AMQP_URI)

    API_TITLE = 'GitResumeWebServiceAPI'
    API_ROUTER_V1 = '/api/v1'
    API_BASE_PREFIX = '/git-resume'

    GITHUB_RESUME_SERVICE = 'GitHubResume'

    @property
    def redis_config(self) -> dict:
        return {
            'host': self.REDIS_HOST,
            'port': self.REDIS_PORT,
            'username': self.REDIS_USER,
            'password': self.REDIS_PASSWORD,
            'db': 0,
            'charset': 'UTF-8',
            'decode_responses': True,
        }

    @property
    def api_config(self) -> dict:
        return {
            'title': self.API_TITLE,
        }

    @property
    def amqp_config(self) -> dict:
        return {
            'AMQP_URI': self.AMQP_URI
        }


config = Config()
