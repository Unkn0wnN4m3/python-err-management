class UsernameException(Exception):

    def __init__(self) -> None:
        super().__init__('Username is not valid')

    def is_valid_to_raise(self):
        return len(self.__notes__) > 0

    def show_notes(self):
        for note in self.__notes__:
            print(note)


def username_validation(username):
    username_error = UsernameException()

    if len(username) <= 5:
        username_error.add_note('Username lenght must be at least 5 chars')

    if username.lower() == 'jc':
        username_error.add_note('Username can\'t be "JC"')

    if '@' in username:
        username_error.add_note('"@" can\'t be in username')

    if username_error.is_valid_to_raise():
        raise username_error

    return True


try:
    username = 'JC'
    username_validation(username)

except UsernameException as error:
    print(error)
    error.show_notes()

finally:
    print("Code done")
