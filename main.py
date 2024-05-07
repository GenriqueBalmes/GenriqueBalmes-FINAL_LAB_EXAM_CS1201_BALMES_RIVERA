def main():
    print("\nWelcome to Dice Roll Game!")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("What is your input?")

    if choice == "1":
        Register()
    elif choice == "2":
        Login()
    elif choice == "3":
        sys.exit()
    else:
        print("Invalid Input")


class GameSystem:
    def __init__(self):
        self.user = {}
        
    def register(self):
        print("Register:")
        username = input("Enter your username (4 characters long) :")
        password = input("Enter your password (8 characters long)")

        if len(username) == 4 and len(password) == 8:
            self.users[username] = password
            print("Registration successful")
        
        else:
            print("Invalid username or password length")
    
    def login(self):
        print("Login")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        



