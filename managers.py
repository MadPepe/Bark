import sqlite3
from os.path import exists as path_exists
from os import mkdir


class DatabaseManger:
    def __init__(self, file_path="Data"):
        self.database_directory = self._get_or_create_relative_directory(file_path)
        self.connection = sqlite3.connect(self.database_directory)

    def __del__(self):
        self.connection.close()

    def _execute(self, query, values=None):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(query, values or [])
            return cursor

    @staticmethod
    def _get_or_create_relative_directory(directory):
        if not path_exists(directory):
            mkdir(directory)
        return f"{directory}/database.db"
