# 1. Define funtion to validate name
def valid_name(name):
    return name.isalpha()

# 2. Define function to validate age
def valid_age(age):
    return age.isdigit() and int(age) >= 0

# 3. Initialize list for storing data
people_info = []

# 4. Loop for user input
while True:
    name = input("Enter your name: ").strip()

    if not valid_name(name):
        print("Error! Only alphabetic characters are allowed.")
        continue