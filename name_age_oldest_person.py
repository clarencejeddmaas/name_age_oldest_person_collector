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

    # 7. Ask for another entry
    another_entry = input("Do you want another entry? (YES or NO): ").strip().lower()

    # 8. Exit loop if no more entries
    if another_entry == 'no':
        break

# 9. Find the oldest person
oldest_person = None
for person in people_info:
    if oldest_person is None or person["age"] > oldest_person["age"]:
        oldest_person = person

# 10. Display the person's information
if oldest_person:
    print(f"The oldest person is {oldest_person['name']} who is {oldest_person['age']} years old.")
else:
    print("No entries were made.")