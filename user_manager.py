class UserManager:

    def __init__(self):
        self.user_file = 'users.txt'
        self.users = self.load_user()

    def load_users():
        users = {}

        with open('users.txt','r') as file:
            for line in file:
                username, password = line.strip().split(" , ")
                users[username] = password

    def save_users(self, username, password):
        pass


    def validate_username():
        pass

    def validate_password():
        pass

    def register(self):
        print("Register:")
        username = input("Enter your username (4 characters long) :")
        password = input("Enter your password (8 characters long)")

        if len(username) == 4 and len(password) == 8:
            self.users[username] = password
            print("Registration successful")
        
        else:
            print("Invalid username or password length")
        
    def login():
        pass
