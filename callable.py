from typing import TypeVar, Generic
from logging import Logger, getLogger


T = TypeVar('T')

class LoggedVar(Generic[T]):
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:
        self.log('Set ' + repr(self.value))
        self.value = new

    def get(self) -> T:
        self.log('Get ' + repr(self.value))
        return self.value

    def log(self, message: str) -> None:
        self.logger.info('{}: {}'.format(self.name, message))

# lv = LoggedVar[int](89, "dom", 5)

logger = getLogger(__name__)

my_var = LoggedVar(42, 'my_var', logger)
print(my_var.log("hello"))
my_var.set(23)
print(my_var.get())
