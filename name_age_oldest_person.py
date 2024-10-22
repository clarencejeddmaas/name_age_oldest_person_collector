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
        print("Error! Only alphabetic characters allowed.")
        continue

    # 5. Loop for age input
    while True:
        age = input("Please enter your age: ").strip()
        
        if not valid_age(age):
            print("Error! Only non-negative numbers are allowed.")
            continue 
        else:
            age = int(age) 
            break
    
    # 6. Store name and age in list
    people_info.append({"name": name, "age": age})