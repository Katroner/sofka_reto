import sqlite3


class Connection:
    def __init__(self) -> None:
        self.__error = ""
        self.__data = []

    # Getters
    def get_error(self) -> str:
        return self.__error

    # Properties
    error = property(get_error)

    # Public methods
    def select(self, query: str) -> list:
        try:
            with sqlite3.connect("/db/questions.db") as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                self.__data = cursor.fetchall()

                return self.__data

        except Exception as e:
            self.__error = str(e)

    def upload_insert(self, query: str, data: tuple) -> None:
        try:
            with sqlite3.connect("/db/questions.db") as conn:
                cursor = conn.cursor()
                cursor.execute(query, data)
                conn.commit()

        except Exception as e:
            self.__error = str(e)
