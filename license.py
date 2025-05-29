import re

from validator import license_validator


class License:
    def __init__(self, id, name, family, license_number, license_date, license_type):
        self.id = id
        self.name = name
        self.family = family
        self.license_number = license_number
        self.license_date = license_date
        self.license_type = license_type

    def save(self):
        print(f"{self.id} {self.name} {self.family} {self.license_number} saved")

    def validate(self):
        return license_validator(self)

    def to_tuple(self):
        return (self.id, self.name, self.family, self.license_number, self.license_date, self.license_type)
