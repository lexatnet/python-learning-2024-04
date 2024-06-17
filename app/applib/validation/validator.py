from abc import ABC, abstractmethod


class Validator(ABC):
    def __init__(self, params):
        self.params = params

    @abstractmethod
    def validate(self, data):
        pass
