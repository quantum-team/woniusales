
from login import login
from register import register

def main():
    print('{:*^60}'.format(' 欢迎来到WoniuSales！'))
    print('{:*^54}'.format(' 1：登录   2：注册   3：修改密码 '))
    choice = input('请选择：')
    if choice == '1':
        login()
    elif choice == '2':
        register()
    elif choice == '3':
        change_pw()
    else:
        print('输入的选项不正确，请重新输入！')

main()
