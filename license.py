import re
class License:
    def __init__(self,id,name,family,license_number,data,license_type):
        self.id = id
        self.name = name
        self.family = family
        self.license_number = license_number
        self.data = data
        self.license_type = license_type
    def save(self):
        print(f"{self.id} {self.name} {self.family} {self.license_number} saved")


    def license_validator(self):
        errors = []
        if not (type(self.id) == int and self.id > 0):
            errors.append('Person ID must be an integer > 0')

        if not (type(self.name) == str and re.match(r"^[a-zA-Z\s]{3,30}$", self.name)):
            errors.append('Person Name is Invalid')

        if not (type(self.family) == str and re.match(r"^[a-zA-Z\s]{3,30}$", self.family)):
            errors.append('Person Family is Invalid')

        if not (type(self.license_number) == str and re.match(r"^\d{8}$", self.license_number)):
            errors.append('Person License Number is Invalid')

        if not (type(self.data) == str and re.match(r"^\d{4}[-/](0[1-9]|1[0-2])[-/](0[1-9]|[12][0-9]|3[01])$",
                                                     self.data)):
            errors.append('Issue Date')

        if not (type(self.license_type) == str and re.match(r"^[a-zA-Z\s\d]{2,15}$", self.license_type)):
            errors.append('lisense is Invalid')

        return errors
