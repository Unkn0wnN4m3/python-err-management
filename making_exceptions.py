class UserLenghtException(Exception):

    def __init__(self, username) -> None:
        self.username = username
        self.message = '"{}" needs at least 5 characters'.format(username)

        # NOTE: Con la funcion "super()" podemos acceder a la funcion "__ini__"
        # de la clase padre. En este caso Exception
        super().__init__(self.message)


def validate_username(username):
    if len(username) <= 5:
        raise UserLenghtException(username)
    return True


try:
    username = "JC"
    result = validate_username(username)

except Exception as error:
    print("Error found:", error)

else:
    print(result)
