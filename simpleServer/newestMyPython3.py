#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'EnDian personal Python3 module'

from datetime import datetime,timedelta #使用date相关
import sys
import os
import pickle       #使用pickle持久化对象
import sqlite3      #使用sqlite3要导入的
from functools import reduce    #导入reduce方法
from multiprocessing import Process
import threading
from collections import OrderedDict  
import time
#import pygame
#Key有序的dict,为了定义的类能和生成表的顺序一样而用
#import virtkey #模拟按键的。。。
import time #睡眠的。。。
import signal #定时输入的，仅linux...
#import eyed3 #获得mp3相关信息，包括长度的

##########################为求正确显示希伯来语#######
hebrew_辅音集 = 'ק ר א ט ו ן ם פ ש ד ג כ ע י ח ל ך ף ז ס ב ה נ מ צ ת ץ ! ( ) / ? ？\\'
def is_FuYin(char):
    if char in hebrew_辅音集:
        return True
    else:
        return False

def eat2list(hebrews):
    list4heb = []
    one_heb = ''
    isFirst = True
    for one in hebrews:
        if isFirst:
            isFirst = False
            one_heb = one
            continue
        if is_FuYin(one):
            list4heb.append(one_heb)
            one_heb = one
        else:
            one_heb = one_heb + one
    list4heb.append(one_heb)
    return list4heb

def heb_list2text(list4heb):
    text = ''
    list4heb = list4heb[::-1]
    for heb in list4heb:
        if heb == ')':
            heb = '('
        elif heb == '(':
            heb = ')'
        text += heb
    #text += ' █'
    text += ' ◀'
    return text

def right_heb(hebrews):
    return heb_list2text(eat2list(hebrews))

#print(right_heb('הוׂדוּ  לַיהוה(אֲדֹנָי) כִּי  טוׂב!'))

##########################显示notify-send信息#########
def show_UI(show_mes='Hello'):
    runsyscmd('notify-send \'%s\'' % show_mes)
##########################显示notify-send信息#########



###########################cvlc放音乐带快慢############
##########这个专门为放bt音乐而改动了点。。。###########
def cvlc_play_mp3(file_name, loops=1, key1='s', key2='f', hasBlank=False):
    file_names = ''
    if hasBlank:
        file_name = file_name.replace(' ', '\ ')
    for i in range(loops):
        file_names = file_names + file_name + ' '
    play_cmd = 'cvlc --global-key-rate-slower-fine \'%s\' --global-key-rate-faster-fine \'%s\' --play-and-exit %s > /dev/null 2>&1' % (key1, key2, file_names)
    #print(play_cmd) #原来一直重复是因为vlc设置了循环。打开vlc关掉循环，行了。。。
    runsyscmd(play_cmd, 'no_print')
###########################cvlc放音乐带快慢############




###########################获得歌曲长度############
#def get_mp3_length(file_name):
    #return eyed3.load(file_name).info.time_secs
    #想关掉Warning,得修改mp3/header.py的文件
###########################获得歌曲长度############




############################定时输入#################
class InputTimeoutError(Exception):
    pass
def interrupted(signum, frame):
    raise InputTimeoutError
def time_input(show_message='input:', time4input=3):
    signal.signal(signal.SIGALRM, interrupted)
    signal.alarm(time4input)
    try:
        data = input(show_message)
    except InputTimeoutError:
        #print('timeout.')
        data = 'time_out'
    signal.alarm(0)
    return data
############################定时输入#################




############################播放音乐至回车##########
def play_enter(voice_file, time4input=1, times=2):
    while True:
        cvlc_play_mp3(voice_file, times, '-', '=')
        CMD = time_input('', time4input=time4input)
        if CMD != 'time_out':
            return CMD
###################################################





########################播放mp3文件###############
#def playmp3(file_name, loops=1, sleep_time=1):
    #pygame.mixer.init() #初始化音频
    #track = pygame.mixer.music.load(file_name)#载入音乐文件
    ##play(pygame.seconds())
    #for i in range(loops):
        #pygame.mixer.music.play()#开始播放
        #while pygame.mixer.music.get_busy() == 1:
            #time.sleep(1)#播放期间检测放完没
        #if time_input(':', sleep_time) == 'p':
            #input('回车继续')
    #pygame.mixer.music.stop()#停止播放
########################播放mp3文件###############




######################判断文件（夹）存在与否########
def file_exist(file_name):
    return os.path.exists(file_name)
######################判断文件（夹）存在与否########




######################模拟一次按键#####################
#vk = virtkey.virtkey()
#def press_key(KEY, v=vk):
    #v.press_unicode(ord(KEY))
    #v.release_unicode(ord(KEY))
######################模拟一次按键#####################




######################睡眠，默认为3S#######################
def sleep_ed(TIME=3):
    time.sleep(TIME)
######################睡眠#################################




######################打印分割线，默认为_...#####################
def print_(char='_', times=40):
    linestring = ''
    for i in range(times):
        linestring += char
    print(linestring)
######################打印分割线，默认为_...#####################




######################运行多进程或多线程#####################
def runprocess(func, *args):
    p = Process(target=func, args=args)
    p.start()
    #p.join()
def runthread(func, *args):
    t = threading.Thread(target=func, args=args)
    t.start()
######################运行多进程或多线程#####################




######################得到系统命令的参数们（没有自身）#####################
def getcmdargs(): 
    return sys.argv[1:]
######################得到系统命令的参数们（没有自身）#####################




######################获取当前时间的年月日时分秒/年月日/秒数#####################
def getnowtime( a='ymd' ):
    now = datetime.now()
    if a == 'ymd':
        return now.strftime('%Y%m%d')

    elif a == 'md':
        return now.strftime('%m%d')

    elif a == 'd':
        return now.strftime('%d')

    elif a == 'ymdhms':
        return now.strftime('%Y%m%d%H%M%S')

    elif a == 'week':
        return now.strftime('%w')

    elif a == 'hm':
        return now.strftime('%H%M')

    else:
        return now.timestamp()
######################获取当前时间的年月日时分秒/年月日/秒数#####################




######################获取几天后的年月日##########################################
def getdaystime( day ):
    now = datetime.now()
    now = now + timedelta(days=day)
    return now.strftime('%Y%m%d')
######################获取几天后的年月日##########################################




######################文件直接写入，读取(text)####################################
def write2file(filename, stext):
    with open(filename, 'w') as f:
        f.write(stext)
def readffile(filename):
    with open(filename, 'r') as f:
        return f.read()
######################文件直接写入，读取(text)####################################




######################pickle来进行对象序列化（持久化对象)#####################
def dump2file(filename, obj):
    with open(filename, 'wb') as f:
        pickle.dump(obj, f)
def loadffile(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)
######################pickle来进行对象序列化（持久化对象)#####################




######################打开sqlite3数据库，返回conn和cursor#####################
def opendb(dbname='MyPython3.sqlite'):
    conn = sqlite3.connect(dbname)
    return conn, conn.cursor()
#####################接收一个cursor，并用此执行sql语句，返回values.#######
def runsql(cursor, sql):
    cursor.execute(sql)
    return cursor.fetchall()
######################关闭连接和游标##########################################
def closedb(conn, cursor):
    cursor.close()
    conn.commit()
    conn.close()
##############################################################################




######################获取字体#################################################
Fonts = ['Times', 'Helvetica', 'Courier', 'Symbol', 'Arial', '浪漫雅圆', ('Microsoft YaHei')]
def getfont(fontnumber=6, fontsize=150):
    if len(str(fontnumber))>1:
        return '-*-%s-*-*-*--*-%d-*' % (fontnumber, fontsize)
    fontdescriptor = Fonts[fontnumber]
    return '-*-%s-*-*-*--*-%d-*' % (fontdescriptor, fontsize)
######################获取字体#################################################



   
######################运行系统命令##########################################
def runsyscmd(cmd='clear', print_yes='yes'):
    output = os.popen(cmd)
    if print_yes == 'yes':
        print(output.read())
    else:
        output.read()
    output.close()
######################运行系统命令##########################################




######################返回圣经卷数与卷名dict#################################
def getbiblenamedict(num_name=True, language='Chinese'):
    BibleDictChinese = {1:'创世记', 2:'出埃及记', 3:'利未记', 4:'民数记', 5:'申命记', 6:'约书亚记', 7:'士师记', 8:'路得记', 9:'撒母耳记上', 10:'撒母耳记下', 11:'列王纪上', 12:'列王纪下', 13:'历代志上', 14:'历代志下', 15:'以斯拉记', 16:'尼希米记', 17:'以斯帖记', 18:'约伯记', 19:'诗篇', 20:'箴言', 21:'传道书', 22:'雅歌', 23:'以赛亚书', 24:'耶利米书', 25:'耶利米哀歌', 26:'以西结书', 27:'但以理书', 28:'何西阿书', 29:'约珥书', 30:'阿摩司书', 31:'俄巴底亚书', 32:'约拿书', 33:'弥迦书', 34:'那鸿书', 35:'哈巴谷书', 36:'西番雅书', 37:'哈该书', 38:'撒迦利亚书', 39:'玛拉基书', 40:'马太福音', 41:'马可福音', 42:'路加福音', 43:'约翰福音', 44:'使徒行传', 45:'罗马书', 46:'哥林多前书', 47:'哥林多后书', 48:'加拉太书', 49:'以弗所书', 50:'腓立比书', 51:'歌罗西书', 52:'帖撒罗尼迦前书', 53:'帖撒罗尼迦后书', 54:'提摩太前书', 55:'提摩太后书', 56:'提多书', 57:'腓利门书', 58:'希伯来书', 59:'雅各书', 60:'彼得前书', 61:'彼得后书', 62:'约翰一书', 63:'约翰二书', 64:'约翰三书', 65:'犹大书', 66:'启示录'}
    BibleDictEnglish = {1:'Genesis', 2:'Exodus', 3:'Leviticus', 4:'Numbers', 5:'Deuteronomy', 6:'Joshua', 7:'Judges', 8:'Ruth', 9:'Samuel 1', 10:'Samuel 2', 11:'Kings 1', 12:'Kings 2', 13:'Chronicles 1', 14:'Chronicles 2', 15:'Ezra', 16:'Nehemiah', 17:'Esther', 18:'Job', 19:'Psalms', 20:'Proverbs', 21:'Ecclesiastes', 22:'Song of Songs', 23:'Isaiah', 24:'Jeremiah', 25:'Lamentations', 26:'Ezekiel', 27:'Daniel', 28:'Hosea', 29:'Joel', 30:'Amos', 31:'Obadiah', 32:'Jonah', 33:'Micah', 34:'Nahum', 35:'Habakkuk', 36:'Zephaniah', 37:'Haggai', 38:'Zechariah', 39:'Malachi', 40:'Matthew', 41:'Mark', 42:'Luke', 43:'John', 44:'Acts', 45:'Romans', 46:'Corinthians 1', 47:'Corinthians 2', 48:'Galatians', 49:'Ephesians', 50:'Philippians', 51:'Colossians', 52:'Thessalonians 1', 53:'Thessalonians 2', 54:'Timothy 1', 55:'Timothy 2', 56:'Titus', 57:'Philemon', 58:'Hebrews', 59:'James', 60:'Peter 1', 61:'Peter 2', 62:'John 1', 63:'John 2', 64:'John 3', 65:'Jude', 66:'Revelation'}
    if num_name and language == 'Chinese':
        return BibleDictChinese
    elif num_name and language == 'English':
        return BibleDictEnglish
    elif language == 'Chinese':
        bd = {} #准备反转上面的字典
        for k, v in BibleDictChinese.items():
            bd[v] = k
        return bd
    elif language == 'English':
        bd = {} #准备反转上面的字典
        for k, v in BibleDictEnglish.items():
            bd[v] = k
        return bd
######################返回圣经卷数与卷名dict#################################




######################ORM框架###############################################
######################Field类——字段类######################
class Field(object):
    def __init__(self, name, column_type):
        self.name = name    #表的字段名，用户提供
        self.column = column_type   #字段类型，细化提供
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)
######################细化Field类——各个类型字段类，不用用户传类型了
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(200)')
class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'integer')
class PrimaryField(Field):
    def __init__(self, name):
        super(PrimaryField, self).__init__(name, 'integer primary key')
######################Field类——字段类######################

######################ModelMetaclass，元类（生成类对象）开始
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):#生成类对象用的，实际生成类对象class Model时调用。没错，就是这里～当然，后来用它生成的Model来生成的对象也得调用下这个方法，如Class User
        if name=='MyORM':    #不修改这个自己提供出去的基类
            #print('生成Model类对象')
            return type.__new__(cls, name, bases, attrs)

        #else : #嗯，其他的类定义时也会调用这个，证明了～
            #print('生成其他类对象')
            #return type.__new__(cls, name, bases, attrs)

        #print('Found model:%s' % name)  #报告，用户使用基类定义类了
        if attrs.get('cursor', 'No') == 'No' or attrs.get('conn', 'No') == 'No' or attrs.get('tableInfo', 'No') == 'NO': #没定义cursor or conn or tableInfo
            print('NoCursorOrConnOrTableInfo.EXIT...') #报告，没cursor/conn/tableInfo，撤
            exit()
        #能直接在类定义里里把外面的cursor等东西传进去

        mappings = OrderedDict()   #准备存{'ID'：IntegerField('id')}的东西,有序字典
        for k in attrs['tableInfo']: #遍历{'ID':IntegerField('id')}们，也是有序字典
            mappings[k] = attrs['tableInfo'][k] #保存用户定义的字段（列）
        attrs['__mappings__'] = mappings #给用户定义的类加个属性和值（保存用户定义的表）

        ######################################################################################
        #####用户定义类时，根据类名，列名创建表，如果已经有创建了，打印创建表的语句。。。#####
        coltype = [] #提取出列名和列属性们创建表
        for k in mappings: #遍历{'ID':IntegerField('id')}们来获得方便数据库操作的列
            v = mappings[k]
            coltype.append(v.name + ' ' + v.column) #存储了表名 表类型，username varchar(100)这样。

        #遍历此list，元素为"表名 表类型"字串，生成新的一个字串，分割符为","。id integer, uname varchar...
        columntype = ','.join(coltype) 
        try:
            attrs['cursor'].execute('create table %s (%s)' % (name,columntype))
        except:
            pass
            #print('create table %s (%s)' % (name,columntype)) #name是用户定义的类名
        ######################################################################################

        attrs['__table__'] = name #假设表名与用户定义的类名一致，保存表名
        return type.__new__(cls, name, bases, attrs) #来，你的类，改了一通，啥都没少，给你。（用户定义的是未知的，无法在下面魔术方法里使用，改了，是已知的了，就是__mappings__和__table__，可以替用户完成处理这些的繁琐的工作了
######################ModelMetaclass，元类（生成类对象）开始

#提供给用户的基类对象Model
class MyORM(dict, metaclass=ModelMetaclass): #元类处理后生成的一个字典类MyORM.有序字典，能够使定义类和生成表一致
    def __init__(self, **kw): #是在生成对象时调用，实参
        self.init() #初始化，生成IDid来方便用ID来找id
        super(MyORM, self).__init__(**kw) #上抛用户实参，交给父类dict来生成对象。

    def __getattr__(self, key): #获得'ID'们对应的列对象
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"No attribute %s" % key)

    def __setattr__(self, key, value):
        self[key] = value #动态增加一个对象名和列对象

    def init(self): #（原save方法）初始化方法，得到IDid（ID和id的关系）
        self.IDid = {} #保存ID-id的关系，方便用ID查找
        for k in self.__mappings__: #遍历{'ID':IntegerField('id')}们来获得方便数据库操作的列，？，值
            v = self.__mappings__[k]
            self.IDid[k] = v.name

    def add(self, **kw): #保存（在自己表中增加一行）的方法
        fields = [] #列们
        params = [] #列们对应的参数占位符们
        args = [] #列位/参数占位符们对应的实际参数们
        for k, v in kw.items():
            fields.append(self.IDid[k]) #通过列对象得到列名
            params.append('?') #一个列一个占位符
            args.append(v) #实参数们
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        #print(sql, str(args))
        self.cursor.execute(sql, args) #嗯，只能这样用，不能直接把实参用%s替换进去，不懂~
        self.updb() #更新数据库
        #print('Added...')

    def delete(self, NAME, value):
        sql = 'delete from %s where %s=?' % (self.__table__, self.IDid[NAME]) #得这样才能正确查询，不能直接替换实参~
        #print(sql)
        self.cursor.execute(sql, (value,)) #管他理解不理解呢，能用，知道怎么用，好好用。。。
        self.updb() #更新数据库

    def update(self, * , NAME, value, **kw): #得提交过的才能查询并修改。。。没提交的可不行。。。
        setlist = []
        valuelist = []
        for k, v in kw.items():
            setlist.append(self.IDid[k]+'=?')
            valuelist.append(v)
        valuelist.append(value)
        sql = 'update %s set %s where %s=?' % (self.__table__, ','.join(setlist), self.IDid[NAME])
        #print(sql, valuelist)
        self.cursor.execute(sql, valuelist) #嗯，只能这样用，不懂
        self.updb() #更新数据库
        sql = 'select * from %s where %s=?' % (self.__table__, self.IDid[NAME])
        print((self.cursor.execute(sql, (value,))).fetchall())

    def find(self, NAME='ALLField', value=None):
        if NAME=='ALLField':
            sql = 'select * from %s' % self.__table__
            return self.cursor.execute(sql).fetchall() #管他理解不理解呢，能用，知道怎么用，好好用。。。
        else:
            sql = 'select * from %s where %s=?' % (self.__table__, self.IDid[NAME])
            return self.cursor.execute(sql, (value,)).fetchall() #带参数查询要这样，直接替换字串参数，有不理解的错误，这样能正确查询

    def updb(self): #得先更新数据库才能用里面的数据。。。不然可没法用。。。得退出才能用。。。
        self.conn.commit()
######################ORM框架###############################################



######################测试新方法##########################################
if __name__ == '__main__':
    try:
        tablettt = OrderedDict()
        conn, cursor = opendb()
        tablettt['F'] = StringField('first') #行，能按顺序来了。。。
        tablettt['ID'] = PrimaryField('id') #生成这个自增的列对象，不用管。。。由PField改为ID，可用，只要不改后面的就行
        tablettt['STRING'] = StringField('string1') #生成一个名为STRING的列对象
        tablettt['T'] = StringField('testcolumn') #行，能按顺序来了。。。
        tablettt['L'] = StringField('last') #行，能按顺序来了。。。
        class TTtable(MyORM): #类名即表名。如果修改定义，需要删除原来表，重新建个新表。。。约为不能修改。。。
            conn = conn
            cursor = cursor #需要传入这三个,conn,cursor,tableInfo
            tableInfo = tablettt
        
        #生成的对象，最好用全局变量，这样，调用时候不用繁琐的传参数了～～～

        ##4个方法方便查看
        def add(self, **kw): 
            pass
        def delete(self, NAME, value):
            pass
        def update(self, * , NAME, value, **kw): 
            pass
        def find(self, NAME='ALLField', value=None):
            pass
    finally:
        closedb(conn,cursor)
    pass #可以从这里加测试代码

    


__author__ = 'JiangEndian'
