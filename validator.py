import re


def license_validator(license):
    errors = []
    if not (type(license.id) == int and license.id > 0):
        errors.append('Person ID must be an integer > 0')

    if not (type(license.name) == str and re.match(r"^[a-zA-Z\s]{3,30}$", license.name)):
        errors.append('Person Name is Invalid')

    if not (type(license.family) == str and re.match(r"^[a-zA-Z\s]{3,30}$", license.family)):
        errors.append('Person Family is Invalid')

    if not (type(license.license_number) == str and re.match(r"^\d{8}$", license.license_number)):
        errors.append('Person License Number is Invalid')

    if not (type(license.license_date) == str and re.match(r"^\d{4}[-/](0[1-9]|1[0-2])[-/](0[1-9]|[12][0-9]|3[01])$",
                                                        license.license_date)):
        errors.append('Issue Date')

    if not (type(license.license_type) == str and re.match(r"^[a-zA-Z\s\d]{2,15}$", license.license_type)):
        errors.append('lisense is Invalid')

    return errors