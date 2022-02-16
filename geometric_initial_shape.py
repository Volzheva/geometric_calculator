from abc import ABC, abstractmethod


class FlatShape(ABC):

    title = 'Плоская фигура'

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            if val <= 0:
                raise ValueError('Вы ввели число меньше нуля или равное нулю.')
            setattr(self, key, val)

    @property
    @abstractmethod
    def area(self):
        ...

    @property
    @abstractmethod
    def perimeter(self):
        ...


class VolumetricShape(FlatShape):

    title = 'Объемная фигура'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    @abstractmethod
    def volume(self):
        ...

