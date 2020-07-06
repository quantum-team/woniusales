from utils import Mysql
from utils import encrypt
## 初始化4个登录用户
default_userinfo = '''insert into user(username, passwd, role, realname, phone) values('admin', '21232f297a57a5a743894a0e4a801fc3', '0', '管理员', '10086'),
                            ('dianyuan1', 'bec8ee5aa927c15b828fc6acf3461129', '2', '店员1', '13800000001'),
                            ('dianyuan2', 'ce97c31e8e2272bd3cca8a5f06074086', '2', '店员2', '13800000002'),
                            ('boss', '4988ec12e3d9a8db3943f47d4ca37c62', '1', '老板', '13800000000')'''
## 初始化3个角色等级
default_role = '''insert into role(role, rolename) values('0', '管理员'), ('1', '老板'), ('2', '店员')
                    '''
## 写入数据库
userinfo = Mysql().insert_IDback(default_userinfo)
role = Mysql().insert_IDback(default_role)
## 写入结果，数字则写入成功，False为失败
print(userinfo, role)