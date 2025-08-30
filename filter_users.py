import json


def filter_users_by_name(name):
    """
    Filtering the users with matching name from json file users.json
    :param name: Name as string
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    """
    Filtering the users with matching age from json file users.json
    :param age: Age as integer
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == age]

    for user in filtered_users:
        print(user)


def filter_users_by_email(email):
    """
    Filtering the users with matching email from json file users.json
    :param email: email as string
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"] == email]

    for user in filtered_users:
        print(user)

if __name__ == "__main__":
    filter_option = input("What would you like to filter by? ('age' 'name' 'email'): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = int(input("Enter the age to filter users: ").strip())
        filter_users_by_age(age_to_search)
    elif filter_option == "email":
        email_to_search = input("Enter the email to filter users: ").strip()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")
