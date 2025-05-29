import re
class License:
    def __init__(self,id,name,family,license_number,data,license_type):
        self.id = id
        self.name = name
        self.family = family
        self.license_number = license_number
        self.data = data
        self.license_type = license_type
        self.license_list = []
    def save(self):
        print(f"{self.id} {self.name} {self.family} {self.license_number} saved")
    def add_license(self, license):
        self.license_list.append(license)

    def license_validator(self,license):
        errors = []
        if not (type(license[0]) == int and license[0] > 0):
            errors.append('Person ID must be an integer > 0')

        if not (type(license[1]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", license[1])):
            errors.append('Person Name is Invalid')

        if not (type(license[2]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", license[2])):
            errors.append('Person Family is Invalid')

        if not (type(license[3]) == str and re.match(r"^\d{8}$", license[3])):
            errors.append('Person License Number is Invalid')

        if not (type(license[4]) == str and re.match(r"^\d{4}[-/](0[1-9]|1[0-2])[-/](0[1-9]|[12][0-9]|3[01])$",
                                                     license[4])):
            errors.append('Issue Date')

        if not (type(license[5]) == str and re.match(r"^[a-zA-Z\s\d]{2,15}$", license[5])):
            errors.append('lisense is Invalid')

        return errors
