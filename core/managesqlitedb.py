# -*- coding: utf-8 -*-

try:
    import sqlite3 as sqlite
    from src.Colors import TextColor
    import os
except Exception as err:
    raise SystemError, TextColor.RED + str("Something is wrong with libreries " + err) + TextColor.WHITE


class DirectoryFinerDB():
    def __init__(self):
        dbPath = os.getcwd() + "/core/dbs/dirbrute.db"
        if os.path.exists(dbPath):
            self.dbConnection = sqlite.connect(dbPath)
            self.__create_table__()
        else:
            print TextColor.RED + str(
                'Something is wrong in database:: database is not exist please create database file') + TextColor.WHITE

    def __create_table__(self):
        try:
            cur = self.dbConnection.cursor()
            cur.execute("""create table if not exists tbl_dirs (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                             path varchar(100) not null unique);""")
            self.dbConnection.commit()
        except sqlite.Error as error:
            print TextColor.RED + str(error) + TextColor.WHITE

    def __insert_data__(self, value):
        try:
            conn = self.dbConnection.cursor()
            conn.execute("INSERT INTO tbl_dirs (path) VALUES (?);", value)
            self.dbConnection.commit()
            conn.close()
            return True
        except sqlite.Error as err:
            print TextColor.RED + str(err) + TextColor.WHITE
            return False

    def __raw_query__(self, query):
        """ Selecting data from database
        :param query: you can send your query that you want
        :return: list of data
        """
        try:
            conn = self.dbConnection.cursor()
            results = conn.execute(query)
            ret_results = list()
            for row in results:
                ret_results.append(row)
            return ret_results
        except sqlite.Error as error:
            print TextColor.RED + str(error) + TextColor.WHITE

    def __delete_data__(self, path):
        """ You can delete some records that you want
        :param ids: you must pass list of ids
        :return: boolean ==> if success return True then return False
        """
        try:
            cur = self.dbConnection.cursor()
            cmd = "delete from tbl_dirs where path=%s" % (path)
            cur.execute(cmd)
            self.dbConnection.commit()
            cur.close()
            return True
        except sqlite.Error:
            return False

    def __update_data__(self, id):
        """ Update data that exists in database with id
        :param id: Enter the id that you wannt update
        :return: boolean ==> if success return true then return false
        """
        try:
            cur = self.dbConnection.cursor()
            cmd = "update tbl_dirs set path=? where id=%s" % (id)
            cur.execute(cmd, id)
            self.dbConnection.commit()
            cur.close()
            return True
        except sqlite.Error:
            return False


class WebAttackDb:
    def __init__(self):
        dbPath = os.getcwd() + "/core/dbs/webattack.db"
        if os.path.exists(dbPath):
            self.dbConnection = sqlite.connect(dbPath)
            self.__create_table__()
        else:
            print TextColor.RED + str(
                'Something is wrong in database:: database is not exist please create database file') + TextColor.WHITE

    def __create_table__(self):
        try:
            cur = self.dbConnection.cursor()
            cur.execute("""create table if not exists tbl_xss_payloads (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                             payload nvarchar(700) not null unique);""")
            self.dbConnection.commit()
        except sqlite.Error as err:
            print TextColor.RED + str(err) + TextColor.WHITE

    def __insert_data__(self, value):
        try:
            conn = self.dbConnection.cursor()
            conn.execute("INSERT or ignore INTO tbl_xss_payloads (payload) VALUES (?);", value)
            self.dbConnection.commit()
            conn.close()
            return True
        except sqlite.Error as error:
            print TextColor.RED + str(error) + TextColor.WHITE
            return False

    def __raw_query__(self, query):
        """ Selecting data from database
        :param query: you can send your query that you want
        :return: list of data
        """
        try:
            conn = self.dbConnection.cursor()
            results = conn.execute(query)
            ret_results = list()
            for row in results:
                ret_results.append(row)
            return ret_results
        except sqlite.Error as err:
            print TextColor.RED + str(err) + TextColor.WHITE

    def __delete_data__(self, path):
        """ You can delete some records that you want
        :param ids: you must pass list of ids
        :return: boolean ==> if success return True then return False
        """
        try:
            cur = self.dbConnection.cursor()
            cmd = "delete from tbl_xss_payloads where payload=%s" % (path)
            cur.execute(cmd)
            self.dbConnection.commit()
            cur.close()
            return True
        except sqlite.Error:
            return False

    def __update_data__(self, id):
        """ Update data that exists in database with id
        :param id: Enter the id that you wannt update
        :return: boolean ==> if success return true then return false
        """
        try:
            cur = self.dbConnection.cursor()
            cmd = "update tbl_xss_payloads set payload=? where id=%s" % (id)
            cur.execute(cmd, id)
            self.dbConnection.commit()
            cur.close()
            return True
        except sqlite.Error:
            return False
