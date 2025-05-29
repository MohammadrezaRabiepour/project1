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
