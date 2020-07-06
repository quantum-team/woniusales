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
        finally:
            self.close(cursor, connection)
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
def encrypt(passwd: str) -> str:    ## 密码加密函数
    import hashlib
    md = hashlib.md5()
    md.update(passwd.encode())
    return md.hexdigest()
class Getch_Windows:    ## 输入密码星号显示，无需调用，请直接调用pwd_input
    def __init__(self):
        pass
    def pwinput(self, prompt: str = '请输入密码: '):      # 只有按回车键，才会返回实际输入的字符
        import msvcrt, sys
        chars = []
        sys.stdout.write(prompt) # 文字提示用户输入密码
        while True:
            ## getch() 返回的是一个二进制字符，需decode()转换为utf8字符串
            newChar = bytes.decode(msvcrt.getch(), encoding='utf8') # 将用户输入的每一个字符进行操作（每输入一个字符自动确认）
            if newChar in '\r\n':   # 如果是回车键，则返回字符串
                print('')
                return ''.join(chars)   # chars是单个字符列表，此方法将列表转换为一串
            elif newChar ==  '\b':
                if chars:
                    chars.pop() # 按backspace，删除最后一个字符
                    sys.stdout.write('\b \b')   # 显示的字符同样减少一个
            else:
                chars.append(newChar)
                sys.stdout.write('*')   # 将字符显示为*号
    def default_input(self, prompt: str = '请输入密码: '):
        return input(prompt)
def pwd_input(print_str: str) -> str:       ## 输入密码星号显示直接调用eg. pw_input('请输入密码：')
    try:
        return Getch_Windows().pwinput(print_str)
    except:
        print('无法加载星号加密组件，将使用默认输入方式：')
        return Getch_Windows().default_input(print_str)