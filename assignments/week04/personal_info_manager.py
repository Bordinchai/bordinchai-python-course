def display_summary(person_tuple,hobbies_list):
    print("="*35,end='')
    print("PROFILE SUMMARY",end='')
    print("="*35)
    print(f"Name   :   {person_tuple[0]}")
    print(f"Age    :   {person_tuple[1]}")
    print(f"City   :   {person_tuple[2]}")
    print(f"Country:   {person_tuple[3]}")
    print(f"hobbies:   {hobbies_list}")
    print("="*35)

def personal_info_manager():
    name = input("Enter your name: ")
    while True:
        age = int(input("Enter your age: "))
        if age < 0:
            print("Your age cannot be negative! Try again.")
        elif age >= 0:
            break
        else:
            print("Error: Invalid input! Please enter a valid integer for age.")
    city = input("Enter your city: ")
    country = input("Enter your country: ")
    info_list = [name, age, city, country]
    person = tuple(info_list)

    hobbies =[]
    while True:
        hobbie = input("Enter a hobbie(type 'done' to stop): ")
        if hobbie == "done":
            break
        hobbies.append(hobbie)
    display_summary(person,hobbies)
    while True:
        print("Do you want to:")
        print("1. Add a hobby")
        print("2. Delete a hobby")
        print("3. Change Age")
        print("4. Exit")

        choice = int(input("Enter choice (1-4): "))
        if choice == 1:
            print("Enter hobbies to add (type 'done' to stop): ")
            while True:
                hobbie = input("Enter hobby: ")
                if hobbie == 'done':
                    break
                hobbies.append(hobbie)
            display_summary(person, hobbies)
        elif choice == 2:
            if hobbies == []:
                print("No hobbie available to detect!")
                break
            elif hobbie != []:
                print("Enter hobby to remove (type 'done' to stop)")
                while True:
                    hobbie = input("Enter hobby to delete: ")
                    if hobbie == 'done':
                        break
                    if hobbie in hobbies:
                        hobbies.remove(hobbie)
                        print(f"Removed '{hobbie}'.")
                    else:
                        print(f"'{hobbie}' not found in your hobbies list!")
                    display_summary(person,hobbies)
        elif choice == 3:
            while True:
                new_age = int(input("Enter your new age: "))
                if new_age < 0:
                    print("Age cannot be negative!")
                elif new_age >= 0:
                    info_list = list(person)
                    info_list[1] = new_age
                    person = tuple(info_list)
                    print(f"Age successfully updated to {new_age}")
                    display_summary(person, hobbies)
                    break
                else:
                    print("Error:Please enter a valid integer for age.")
                display_summary(person, hobbies)
        elif choice == 4:
            print("Exiting profile manager. Goodbye!")
            break
        else:
            print("Invalid selection! Please choose (1-4)")

personal_info_manager()

