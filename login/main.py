
from login import login

def main():
    print('{:*^60}'.format(' 欢迎来到WoniuSales！'))
    login_check = login()


if __name__ == "__main__":
    main()
    print('success')

