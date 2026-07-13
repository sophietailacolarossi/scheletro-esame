from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getDD():
        cn = DBConnect.get_connection()
        cursor = cn.cursor(dictionary=True)

        res = []
        query = """ """
        cursor.execute(query, )

        for row in cursor:
            res.append(())

        cn.close()
        cursor.close()
        return res

    @staticmethod
    def getNodes():
        cn = DBConnect.get_connection()
        cursor = cn.cursor(dictionary=True)

        res = []
        query = """ """
        cursor.execute(query, )

        for row in cursor:
            res.append(())

        cn.close()
        cursor.close()
        return res

    @staticmethod
    def getAllEdges():
        cn = DBConnect.get_connection()
        cursor = cn.cursor(dictionary=True)

        res = []
        query = """"""
        cursor.execute(query, )

        for row in cursor:
            res.append(())

        cn.close()
        cursor.close()
        return res

