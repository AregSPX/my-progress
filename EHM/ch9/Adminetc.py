class Person:
    """A simple attempt to become a human."""
    def __init__(self, first, last):
        """New person"""
        self.name = first
        self.surname = last
        self.login_attempts = 0
    
    def user_info(self):
        """Gathers info."""
        print(f"Full Name: {self.name.title()} {self.surname.title()}")
        
    def greet_user(self):
        print(f"Hello, {self.name.title()} {self.surname.title()}!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
        
class Admin(Person):
    def __init__(self, first, last):
        super().__init__(first, last)
        self.privileges = Privileges()
  
class Privileges:
    def __init__(self, Privileges = ['can add/delete posts', 'can ban users']):
        self.privileges0 = Privileges

    def show_privileges(self):
        """list admin privileges"""
        for x in self.privileges0:
            print(x)