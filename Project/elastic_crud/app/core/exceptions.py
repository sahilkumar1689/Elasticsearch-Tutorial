class NotFoundError(Exception):
    def __init__(self, message: str):
        self.message = message


class ElasticsearchError(Exception):
    def __init__(self, message: str):
        self.message = message
