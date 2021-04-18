import sqllite3


class DatabaseManger:
    def __init__(self, file_name):
        self.connection = sqlite3.connect(file_name)
