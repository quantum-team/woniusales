import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from Common.utils import pwd_input
from Common.utils import Mysql
from Common.utils import encrypt

def register_username():
    while True:
        account = input('请输入注册的用户名：')
        if account.isalnum():       ## 规避sql注入
            user_select = '''select username from user where username = "%s"; '''
            user_check = Mysql().select_oneback(user_select % account)
            if user_check == None:
                return account
            else:
                print('用户已注册，无需重复注册！')
                return False
        else:
            print('用户名不能包含字符，请重新输入！')
            continue
def register_passwd():
    while True:
        passwd_first = encrypt(pwd_input('请输入新密码：'))  # 调用密码加密输入函数，输入后md5加密储存
        if passwd_first == '':
            print('\n请输入密码...\n')
            continue
        else:
            passwd_second = encrypt(pwd_input('请再次确认密码：')) # 密码二次确认
            if passwd_first == passwd_second:
                return passwd_second
            else:
                print('两次密码输入不一致，请重新输入：')
                continue
def register_phone():
    while True:
        phone = input('请输入注册者的11位手机号：')
        if len(phone) == 11 and phone.startswith('1'):
            return phone
        else:
            print('输入的手机号错误，请重新输入')
            continue
def register():
    '''
        只允许注册店员
        :return 注册成功返回True，注册失败返回False
    '''
    flag_success = False
    while True:
        account = register_username()
        if account != False:
            passwd = register_passwd()
            if passwd != False:
                phone = register_phone()
                realname = input('请输入你的真实姓名：')
                flag_success = True
                break
    if flag_success:
        insert_sql = '''  insert into user(username, passwd, role, realname, phone) values("%s", "%s", "%s", "%s", "%s") '''
        code = Mysql().insert_IDback(insert_sql % (account, passwd, '2', realname, phone))
        if code != None:
            print('注册成功！')
            return True
        else:
            print('注册失败！')
            return False