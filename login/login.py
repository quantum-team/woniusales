import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from Common.utils import pwd_input
from Common.utils import Mysql
from Common.utils import encrypt

def login():
    '''
        函数无需传入参数
        :return 用户名
        :return 用户角色等级，0为管理员，1为老板，2为店员
    '''
    flag_username, flag_passwd = True, False
    while True:
        while flag_username:    ## 账号信息匹配
            account = input('请输入账号：')
            if account.isalnum():       ## 规避sql注入
                user_select = '''select username from user where username = "%s"; '''
                user_check = Mysql().select_oneback(user_select % account)
                if user_check != None:      ## 查询到该账户信息
                    flag_username = False
                    flag_passwd = True
                else:
                    print('无该账户信息，请确认后重试！')
                    continue
        while flag_passwd:
            passwd = encrypt(pwd_input('请输入密码：'))
            passwd_select = '''  select passwd from user where username = "%s";  '''
            passwd_check = Mysql().select_oneback(passwd_select % account)['passwd']
            if passwd == passwd_check:
                role_select = ''' select role from user where username = "%s" '''
                role_id = Mysql().select_oneback(role_select % account)['role']
                print('登录成功！')
                return account, role_id
            else:
                print('登录失败，请重试！')
                flag_username = True
                break
        continue