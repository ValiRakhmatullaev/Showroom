import enum


class CarType(enum.Enum):
    SEDAN = 'Sedan'
    COUPE = 'Coupe'
    CROSSOVER = 'Crossover'
    HATCHBACK = 'Hatchback'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
