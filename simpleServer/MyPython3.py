#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'EnDian personal Python3 module'
#这个东西，大概是用来作用换机器时检测需要装的东西吧，屎堆成为了屎山

from datetime import datetime,timedelta #使用date相关
import sys, os, time, re
import pickle       #使用pickle持久化对象
import sqlite3      #使用sqlite3要导入的
from functools import reduce    #导入reduce方法
from multiprocessing import Process
import threading
from collections import OrderedDict #Key有序的dict,为了定义的类能和生成表的顺序一样而用
import random


###########简体-繁体-big5编码####################
def conSc2ox(sc='简繁转换'):
    tc = convert(sc, 'zh-tw')
    ox = tc.encode('big5')
    return sc, tc, ox
###########简体-繁体-big5编码####################



############测试系统需要安装的东西################
apps = ['xdotool', 'ffmpeg', ]
def need2install():
    cmd = '; '.join(apps)
    print(cmd)
#need2install()
############测试系统需要安装的东西################



#############监控某文件变化###############
#############监控某文件变化###############





##########可视化数据############
def pltData(x_list, y_list):
    plt.plot(x, y)
    plt.show
##########可视化数据############


################正则匹配###########
han = r'.*[\u4e00-\u9fa5].*'
en = r'.*[a-zA-Z].*'
def textInLine(text, line):
    if re.match(text, line):
        return True
    else:
        return False
################正则匹配###########




##############模拟按键###############
#KP_Enter, Escape
def pressKey(key):
    syscmd = f'xdotool key {key};sleep 0.2;'
    #print(syscmd)
    runsyscmd(syscmd)
##############模拟按键###############




##############鼠标点击位置#################
def click1Position(pos, op='1'):
    syscmd1 = f'xdotool mousemove --sync {pos[0]} {pos[1]};sleep 0.2;'
    syscmd2 = f'xdotool click {op};sleep 0.2;'
    syscmd = syscmd1 + syscmd2
    #print(syscmd)
    runsyscmd(syscmd)
##############鼠标点击位置#################




#############精准的mateScreenshot##############
def mateScreenshot():
    runsyscmd('mate-screenshot -a')
    input('Enter to continue:')
#############精准的mateScreenshot##############



#################用cv2显示灰度的图片####################
def showImg(imgName):
    img = cv2.imread('xxx.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #CV2的BGR转成灰度
    cv2.namedWindow('img')
    while True:
        cv2.imshow('img', img)
        if cv2.waitKey() == ord('q'): break #还有这种操作方式。。。
    cv2.destroyAllWindows()
#################用cv2显示灰度的图片####################



################精准检测截图的对象位置################
def loadImageObject(img_name, samples=5): #多些检测点，不然不准
    #return imageObject, imageObjectx, imageObjecty, pixels
    imageObject = Image.open(img_name).convert('RGB')
    imageObjectx = imageObject.size[0]
    imageObjecty = imageObject.size[1]
    #print('x,y:', imageObjectx, imageObjecty)
    
    pixels = [] #只有两个点，会导致，两个涨停的红的靠近时，被视为一个红的，加个点因此
    for i in range(samples):
        #x = int(imageObjectx * i/samples) #0, x/3, x2/3 #就是左上角，1/3对角线，2/3对角线
        #y = int(imageObjecty * i/samples) #0, x/3, x2/3
        x = random.randint(1, imageObjectx-2) #随机几个点
        y = random.randint(1, imageObjecty-2) #随机几个点
        pixel = imageObject.getpixel((x, y))
        posPix = ((x, y), pixel)
        pixels.append(posPix) #直接原像素即可
    #print('pixels:', pixels)
    return imageObject, imageObjectx, imageObjecty, pixels

def loadScreenShot(img_name_screenshot='imgSS.png', region=(0,0,100,100)): 
    #return imageInput
    if os.path.isfile(img_name_screenshot):
        os.remove(img_name_screenshot)
    pyautogui.screenshot(imageFilename=img_name_screenshot, region=region) 
    #print(f'catched:{region}')
    imageInput = Image.open(img_name_screenshot).convert('RGB') #原来不等于rgb，老出错
    #_screenshot_linux(imageFilename=None, region=None)
    return imageInput

def scanToGetPositions(img_name_object, img_name_screenshot='imgSS.png', region=(0,0,100,100)):
    #return catched, catchedCenter
    imageObject, imageObjectx, imageObjecty, pixels = loadImageObject(img_name_object)
    imageInput = loadScreenShot(img_name_screenshot, region)
    catched = [] #匹配的几组数据
    catchedCenter = [] #匹配的几组数据
    scanned = (0, 0)
    for x in range(imageInput.size[0]): #x*y像素的输入图片的x
        for y in range(imageInput.size[1]): #x*y像素的输入图片的y
            if x < scanned[0] and y < scanned[1]:
                continue
            if x+imageObjectx>region[2] or y+imageObjecty>region[3]:
                continue #如果最终大于边界，导致出错，会使isObj不被置为False
            isObj = True
            #遍历对象的斜线pos和对应的pixel，
            #某点处能作为原点找到obj的特征点就算为obj
            for posPix in pixels: 
                #try:
                #print((x+posPix[0][0], y+posPix[0][1]))
                ipixel = imageInput.getpixel((x+posPix[0][0], y+posPix[0][1])) 
                if not ipixel == posPix[1]:
                    isObj = False
                    break
                #except IndexError:
                    #print('error occurred.')
                    #pass
            if isObj:
                catched.append((x, y))
                catchedCenter.append((x+int(imageObjectx/4), int(y+imageObjecty/4))) #1/2 or
                scanned = (x+imageObjectx, y+imageObjecty)
                print('catched:', catched)
    #print(catched)
    return catched, catchedCenter

def drawCatched(img_name_object='None', img_name_screenshot='imgSS.png', region=(0,0,100,100), newFileName='output.png'):
    imageObject = loadImageObject(img_name_object)[0]
    imageInput = loadScreenShot(img_name_screenshot, region)
    catched, catchedCenter = scanToGetPositions(img_name_object, img_name_screenshot, region)
    #print(catched)
    draw = ImageDraw.Draw(imageInput)
    for catch in catched:
        draw.rectangle((catch[0], catch[1],catch[0]+imageObject.size[0]-1, catch[1]+imageObject.size[1]-1), outline='red')
    imageInput.save(newFileName)
    imageInput.show()

#drawCatched(img_name_object='baiHuo.png', region=(0,0,400,500))
################精准检测截图的对象位置################



##########################显示notify-send信息#########
def show_UI(show_mes='Hello'):
    runsyscmd('notify-send \'%s\'' % show_mes)
##########################显示notify-send信息#########



###########################cvlc放音乐带快慢############
def cvlc_play_mp3(file_name, loops=1, key1='s', key2='f', key3='p'):
    file_names = ''
    file_name = file_name.replace(' ', '\ ')
    for i in range(loops):
        file_names = file_names + file_name + ' '
    play_cmd = 'cvlc --global-key-play-pause \'%s\' --global-key-rate-slower-fine \'%s\' --global-key-rate-faster-fine \'%s\' --play-and-exit %s > /dev/null 2>&1' % (key3, key1, key2, file_names)
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
        CMD = time_input(':', time4input=time4input)
        if CMD != 'time_out':
            return CMD
###################################################




######################判断文件（夹）存在与否########
def file_exist(file_name):
    return os.path.exists(file_name)
######################判断文件（夹）存在与否########




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




######################获取当前时间的年月日时分秒/年月日/秒数################
def getnowtime( a='ymd' ):
    now = datetime.now()
    if a == 'ymd':
        return now.strftime('%Y%m%d')

    elif a == 'y':
        return now.strftime('%Y')

    elif a == 'm':
        return now.strftime('%m')

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
######################获取当前时间的年月日时分秒/年月日/秒数################




######################获取几天后的年月日####################################
def getdaystime( day ):
    now = datetime.now()
    now = now + timedelta(days=day)
    return now.strftime('%Y%m%d')
######################获取几天后的年月日####################################




######################文件直接写入，读取(text)###########################
def write2file(filename, stext):
    with open(filename, 'w') as f:
        f.write(stext)
def readffile(filename):
    with open(filename, 'r') as f:
        return f.read()
def readAllLinesFromFile(filename):
    with open(filename, 'r') as f:
        return f.readlines()
######################文件直接写入，读取(text)###########################




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
