from cryptography.fernet import Fernet
master_pwd = input("What's your password: ")


def view():
    with open("password.txt", "r") as v:
        for line in v:
            data = line.strip()  # to eliminate the \n while printing
            parts = data.split("|")

        if len(parts) == 3:
            plat, user, passwd = parts
            print(f"Platform: {plat} | Username: {user} |  Password: {passwd}")
        else:
            print(f" Skipping malformed or extra field line: {data}")


def add():
    platform = input("Which platform account are you gonna add: ")
    name = input("What's the usernamae of the account: ")
    password = input("Add the secret password: ")

    with open("password.txt", "a") as f:
        f.write(platform+ "|" +name+ "|" +password+ "\n")


while True:
    mode = input("what mode do you wish to enter view or add ").lower()
    if mode == "q":
        break
    elif mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("invalid mode")
        continue
