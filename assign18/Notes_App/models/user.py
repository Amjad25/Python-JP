class User:
    user_name: str
    password: str
    email: str
    full_name: str
    
    def __init__(self, user_name: str, password: str, email: str, full_name: str):
        self.user_name = user_name
        self.password = password
        self.email = email
        self.full_name = full_name

    def __str__(self):
        return f"{self.user_name} {self.password} {self.email} {self.full_name}"
    
    def __repr__(self):
        return str(self)
    

    def to_dict(self):
        return {
            "user_name": self.user_name,
            "password": self.password,
            "email": self.email,
            "full_name": self.full_name
        }
    

    