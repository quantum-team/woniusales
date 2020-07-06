class Mysql:
    def __init__(self):
        pass
    ## 创建mysql连接
    def connect(self):
        '''
        创建mysql连接
        '''
        import pymysql
        try:
            connection = pymysql.connect(host = '103.45.178.14', 
                                                        port = 3306,   
                                                        user = 'root', 
                                                        passwd = '123456', 
                                                        db = 'sales', 
                                                        charset = 'utf8', 
                                                        cursorclass = pymysql.cursors.DictCursor)       # cursorclass指定：游标返回的结果以字典形式返回
            cursor = connection.cursor()
        except Exception as e:
            print('数据库连接失败！' + e)
            return False
        finally:
            return cursor, connection
    def close(self, cur, con) -> None:
        cur.close()
        con.close()
    def select_oneback(self, select: str) -> dict:
        '''
        执行一条select语句，并返回一行结果
        '''
        import pymysql
        try:
            cursor, connection = self.connect()
            cursor.execute(select)
            fetone = cursor.fetchone()
            return fetone
        except:
            print('数据库连接失败~')
            return False
        # finally:
        #     self.close(cursor, connection)
    ## 执行一条select
    def select_allback(self, select: str) -> dict:
        '''
        执行一条select语句，并返回所有结果
        '''
        import pymysql
        try:
            cursor, connection = self.connect()
            cursor.execute(select)
            fetall = cursor.fetchall()
            return fetall
        except:
            return False
        finally:
            self.close(cursor, connection)
    def insert_IDback(self, ins: str) -> int:
        '''
        执行一条insert语句，并返回插入的行号
        '''
        import pymysql
        try:
            cursor, connection = self.connect()
            if cursor.execute(ins) != 0:
                connection.commit()
            else:
                raise ConnectionError
            insertid = int(cursor.lastrowid)
            return insertid
        except:
            connection.rollback()
            return False
        finally:
            self.close(cursor, connection)
    def update(self, up: str) -> bool:
        '''
        执行一条update语句，返回是否成功
        '''
        import pymysql
        try:
            cursor, connection = self.connect()
            n = cursor.execute(up)
            if n != 0:
                connection.commit()
            else:
                raise ConnectionError
            return n
        except:
            connection.rollback()
            return False
        finally:
            self.close(cursor, connection)
    def create(self, create: str) -> bool:
        '''
        执行一条create语句，返回是否成功
        '''
        import pymysql
        try:
            cursor, connection = self.connect()
            n = cursor.execute(create)
            if n != 0:
                connection.commit()
            else:
                raise ConnectionError
            return n
        except:
            connection.rollback()
            return False
        finally:
            self.close(cursor, connection)

