import re


def license_validator(license):
    errors = []
    if not (type(license[0]) == int and license[0]>0):
        errors.append('Person ID must be an integer > 0')

    if not (type(license[1]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", license[1])):
        errors.append('Person Name is Invalid')


    if not (type(license[2]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", license[2])):
        errors.append('Person Family is Invalid')

    if not (type(license[3]) == str and re.match(r"^\d{8}$", license[3])):
        errors.append('Person License Number is Invalid')

    if not (type(license[4]) == str and re.match(r"\d{4}[-/]\d{2}[-/]\d{2}$", license[4])):
        errors.append('Issue Date')

    if not (type(license[5]) == str and re.match(r"^[a-zA-Z\s\d]{2,15}$", license[5])):
        errors.append('lisense is Invalid')

    return errors
