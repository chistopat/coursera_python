import csv
import os
import typing


class CarBase:
    brand: str
    car_type: str
    carrying: float
    photo_file_name: str
    _photo_ext: str

    def __init__(self, brand: str, photo_file_name: str, carrying: str):
        if not all((brand, photo_file_name, carrying)):
            raise ValueError
        self.brand = brand
        self.carrying = float(carrying)
        self.photo_file_name = photo_file_name

        self._photo_ext = self._parse_file_ext(photo_file_name)

    @staticmethod
    def _parse_file_ext(file_name) -> str:
        ext = os.path.splitext(file_name)[1]
        if ext not in ['.jpg', '.jpeg', '.png', '.gif']:
            raise ValueError
        return ext

    def get_photo_file_ext(self) -> str:
        return self._photo_ext


class Car(CarBase):
    car_type: str
    _passenger_seats_count: int

    def __init__(
            self,
            brand : str,
            photo_file_name: str,
            carrying: str,
            passenger_seats_count: str
    ):
        super(Car, self).__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'
        self._passenger_seats_count = int(passenger_seats_count)

    @property
    def passenger_seats_count(self):
        return self._passenger_seats_count

    @classmethod
    def from_dict(cls, entry):
        return cls( brand=entry['brand'],
                    photo_file_name=entry['photo_file_name'],
                    carrying=entry['carrying'],
                    passenger_seats_count=entry['passenger_seats_count'],
                    )


class Truck(CarBase):
    body_width: float = 0.0
    body_height: float = 0.0
    body_length: float = 0.0

    def __init__(self, brand, photo_file_name, carrying, body_whl: str):
        super(Truck, self).__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        whl = self._parse_whl(body_whl)
        self.body_length = whl[0]
        self.body_width = whl[1]
        self.body_height = whl[2]

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length

    @staticmethod
    def _parse_whl(body_whl: str) -> typing.Tuple[float, float, float]:
        try:
            tokens = body_whl.split('x')
            if len(tokens) != 3:
                raise ValueError
            return float(tokens[0]), float(tokens[1]), float(tokens[2])
        except (ValueError, IndexError):
            return 0.0, 0.0, 0.0

    @classmethod
    def from_dict(cls, entry):
        return cls(brand=entry['brand'],
                   photo_file_name=entry['photo_file_name'],
                   carrying=entry['carrying'],
                   body_whl=entry['body_whl'],
                   )


class SpecMachine(CarBase):
    extra: str = ""

    def __init__(self, brand, photo_file_name, carrying, extra):
        super(SpecMachine, self).__init__(brand, photo_file_name, carrying)
        if not extra:
            raise ValueError
        self.extra = extra
        self.car_type = 'spec_machine'

    @classmethod
    def from_dict(cls, entry):
        return cls(brand=entry['brand'],
                   photo_file_name=entry['photo_file_name'],
                   carrying=entry['carrying'],
                   extra=entry['extra'],
                   )


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.DictReader(csv_fd, delimiter=';')
        for entry in reader:
            try:
                if entry['car_type'] == 'car':
                    car_list.append(Car.from_dict(entry))
                elif entry['car_type'] == 'truck':
                    car_list.append(Truck.from_dict(entry))
                elif entry['car_type'] == 'spec_machine':
                    car_list.append(SpecMachine.from_dict(entry))
                else:
                    continue
            except ValueError:
                continue
    return car_list
