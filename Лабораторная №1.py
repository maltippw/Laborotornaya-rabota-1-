import doctest

class Printer:
    def init(self, brand: str, is_color: bool):
        """
        :param brand: Бренд принтера.
        :param is_color: Поддерживает ли принтер цветную печать.
        """
        self.brand = brand
        self.is_color = is_color

    def print_document(self, pages: int) -> None:
        """
        Печать документа.

        :param pages: Количество страниц (должно быть положительным).
        :return: None

        >>> printer.print_document(5)
        """
        ...

    def replace_cartridge(self) -> None:
        """
        Замена картриджа.
        :return: None
        """
        ...

    def scan_document(self) -> str:
        """
        Сканирование документа.

        :return: Строка с сообщением о завершении сканирования.

        >>> printer.scan_document()
        'Документ отсканирован.'
        """
        return "Документ отсканирован."


class Bottle:
    def init(self, volume: float, material: str):
        """
        :param volume: Объем бутылки в литрах (должен быть положительным).
        :param material: Материал бутылки (например, пластик, стекло).
        """
        if volume <= 0:
            raise ValueError("Объем бутылки должен быть положительным.")
        self.volume = volume
        self.material = material

    def fill(self, amount: float) -> None:
        """
        Наполнить бутылку жидкостью.

        :param amount: Количество жидкости в литрах (должно быть положительным).
        :return: None

        >>> bottle.fill(0.5)
        """
        ...

    def drink(self, amount: float) -> None:
        """
        Выпить жидкость из бутылки.

        :param amount: Количество жидкости в литрах (должно быть положительным).
        :return: None

        >>> bottle.drink(0.3)
        """
        ...

    def clean(self) -> None:
        """
        Очистка бутылки.
        :return: None
        """
        ...


class Kettle:
    def init(self, capacity: float, material: str):
        """
        :param capacity: Объем чайника в литрах (должен быть положительным).
        :param material: Материал чайника (например, сталь, стекло, пластик).
        """
        if capacity <= 0:
            raise ValueError("Объем чайника должен быть положительным.")
        self.capacity = capacity
        self.material = material

    def boil_water(self) -> None:
        """
        Кипячение воды.
        :return: None
        """
        ...

    def pour_water(self, amount: float) -> None:
        """
        Наливание воды из чайника.

        :param amount: Количество воды в литрах (должно быть положительным и не превышать объема).
        :return: None

        >>> kettle.pour_water(0.5)
        """
        ...

    def clean(self) -> None:
        """
        Очистка чайника.
        :return: None
        """
        ...


if name == "main":
    doctest.testmod()  # Запуск тестов из документации