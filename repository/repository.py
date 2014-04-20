import sys
sys.path.append('../database')

import sqlite3


class Repository():
    def __init__(self, db_name='../database/zoos.db'):
        self.__connection = self.create_connection(db_name)

    def create_connection(self, db_name):
        return sqlite3.connect(db_name)

    def get_cursor(self):
        return self.__connection.cursor()

    def commit_connection(self):
        self.__conncetion.commit()

    def close_connection(self):
        self.__conncetion.close()

    def is_name_used(self, table, name):
        cursor = self.get_cursor()
        query = "SELECT COUNT(*) FROM {} WHERE name = ?".format(table)
        cursor.execute(query, (name, ))
        count = cursor.fetchone()[0]

        return count > 0

    def __del__(self):
        self.close_connection()
