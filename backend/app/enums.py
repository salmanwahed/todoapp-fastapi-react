import enum


class Gender(enum.Enum):
    MALE = "Male"
    FEMALE = "Female"


class Status(enum.Enum):
    TODO = 'Todo'
    DOING = 'Doing'
    DONE = 'Done'
    LIMBO = 'Limbo'


class Priority(enum.IntEnum):
    IMMEDIATE = 3
    HIGH = 2
    REGULAR = 1
