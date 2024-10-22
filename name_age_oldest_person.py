# 1. Define funtion to validate name
def valid_name(name):
    return name.isalpha()

# 2. Define function to validate age
def valid_age(age):
    return age.isdigit() and int(age) >= 0