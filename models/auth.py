from faker import Faker


fake = Faker("Ru-ru")


class AuthData:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @staticmethod
    def random():
        login = fake.email()
        password = fake.password()
        return AuthData(login, password)
