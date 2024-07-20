class ManageProfile:
    def __init__(self):
        self.profiles = {}

    def create_profile(self, username, profile_data):
        # create a new profile for a user
        self.profiles[username] = profile_data

    def get_profile(self, username):
        # retrieve a user's profile
        return self.profiles.get(username)

    def update_profile(self, username, profile_data):
        # update a user's profile
        self.profiles[username] = profile_data
