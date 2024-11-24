class Password:
    def __init__(self, password):
        self.__password = password

    def verify(self, string):
        if self.__password != string:
            return False
        else:
            return True

my_password = Password("abcd")
print(my_password.verify("abcd"))
print(my_password.verify("azer"))