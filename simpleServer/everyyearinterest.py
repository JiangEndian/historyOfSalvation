#!/usr/bin/env python3

from MyPython3 import *
from table4grace import *

#用前打开生成数据库
def create_database_link():
    global grace_database
    global conn, cursor
    conn, cursor = opendb('database4grace.sqlite')
    class Grace_database(MyORM):
        conn = conn
        cursor = cursor
        tableInfo = tableCommon
    grace_database = Grace_database()

def close_database_link():
    global conn, cursor
    closedb(conn,cursor)


global grace_database

create_database_link() #打开了database4grace.sqlite

all_info = grace_database.find()

#遍历所有信息，来确认之
for one_info in all_info:
    print(one_info)

if not input('你确定这是一年一次(本次应为2021年始)的修改，这将不可退回') == "20220101":
    exit(0)

for one_info in all_info:
    #print(one_info)
    money_interest = int(int(one_info[2])*1.212)
    #因github的无法计算设为0元去掉了加1，而且1.05也确实很高
    #看看5年定期是5.3.嗯。就算为7吧。而且，反正也不还的嘛。。。其实我倒是想10的。。。
    #不对。过了许久是要翻倍的。嗯。旧约是从25-50工作。25年翻倍。算下多少合适：1.028（。）
    #算了。看我所经历的吧。初3生活费，40/5天，每天8块。08年。现在是80,20年。12年共翻10倍
    #则每一年增长率为：0.212。。。。。。。。好。就按这个算吧。毕竟，是这样过来的。。。
    grace_database.update(NAME='ID',value=one_info[0], Money=money_interest)
    #input()

print("Successful!")

