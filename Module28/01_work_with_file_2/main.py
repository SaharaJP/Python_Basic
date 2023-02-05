


class File:
    def __init__(self, file_name: str, type: str = 'w') -> None:
        self.__file_name = file_name
        self.__type = type

    def __enter__(self):
        self.file = open(self.__file_name, self.__type)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file.close()
        return True


with File('test.txt', 'w') as test:
    test.write('Привет!')