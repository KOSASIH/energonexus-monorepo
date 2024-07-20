import hashlib

class UserVerification:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        # register a new user with a username and password
        self.users[username] = hashlib.sha256(password.encode()).hexdigest()

    def verify_user(self, username, password):
        # verify a user's credentials
        if username in self.users:
            return hashlib.sha256(password.encode()).hexdigest() == self.users[username]
        else:
            return False
