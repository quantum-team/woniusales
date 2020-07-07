import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from Common.utils import Mysql

def trans(acc):              # 查询
    sql = 'select * from cap_detail where id=%d;'
    a = Mysql().select_oneback(sql %acc)
    if acc == a['id']:
        return a

def receive(money):        # 转账
    while True:
        sid = input('请输入收款账号：')
        tm = float(input('请输入转账金额：'))
        sql = 'select * from cap_detail where id="%s";'
        if Mysql().select_oneback(sql % sid) == 1:
            m = Mysql().select_oneback(sql = 'select * from capital where money = "%s";')
            if tm > m:
                print('余额不足，请重新输入：')
            else:
                print('转账成功')
                m -= tm
                Mysql().select_oneback(sql = 'select * from capital where id="%s";')
                sql = 'update capital set money="%s";'
                Mysql().update(sql % (money))
        else:
            print('收款账号错误')

if __name__ == '__main__':
    acc = int(input('请输入账号：'))
    print(trans(acc))
    # receive()