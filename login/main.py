
from login import login

if __name__ == "__main__":
    print('{:*^60}'.format(' 欢迎来到WoniuSales！'))
    account, role_id = login()
    if role_id == '0':
        print('欢迎您，管理员！')
    elif role_id == '1':
        print('欢迎您，老板！')
    elif role_id == '2':
        print('欢迎使用WoniuSales，店员！')

