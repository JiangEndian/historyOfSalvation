#!/usr/bin/env python3

from MyPython3 import *
from configurations import *
#runsyscmd()

##################四张表定义#####################
tableCommon = OrderedDict()
tableCommon['ID'] = PrimaryField('id')
tableCommon['Ymd'] = StringField('ymd') #日期
tableCommon['Con'] = StringField('content') #计划内容
tableCommon['Other1'] = StringField('other1') #背景
tableCommon['Other2'] = StringField('other2') #补充们
tableCommon['Other3'] = StringField('other3') #次数加上
############################
tableEveryWeek = OrderedDict()
tableEveryWeek['ID'] = PrimaryField('id')
tableEveryWeek['Day'] = StringField('day') #星期几
tableEveryWeek['Con'] = StringField('content') #计划内容
tableEveryWeek['Other1'] = StringField('other1') #背景
tableEveryWeek['Other2'] = StringField('other2') #补充
tableEveryWeek['Other3'] = StringField('other3')
############################
tableEveryMonth = OrderedDict()
tableEveryMonth['ID'] = PrimaryField('id')
tableEveryMonth['Day'] = StringField('day') #几号
tableEveryMonth['Con'] = StringField('content') #计划内容
tableEveryMonth['Other1'] = StringField('other1') #背景
tableEveryMonth['Other2'] = StringField('other2') #补充
tableEveryMonth['Other3'] = StringField('other3')
############################
tableEveryYear = OrderedDict()
tableEveryYear['ID'] = PrimaryField('id')
tableEveryYear['MonthDay'] = StringField('monthday') #几月几日
tableEveryYear['Con'] = StringField('content') #计划内容
tableEveryYear['Other1'] = StringField('other1') #背景
tableEveryYear['Other2'] = StringField('other2') #补充
tableEveryYear['Other3'] = StringField('other3')
##################四张表定义#####################


##################删除昨天的计划#################
def yesterday(common):
    ystday = getdaystime(-1)
    #print(ystday)
    #print(common.find('Ymd', ystday))
    common.delete('Ymd', ystday)
##################删除昨天的计划#################



##################显示每日计划#####################
##这个是打印文件里面的列表的
#everyday = readffile('everydaytoread.txt')
#print(everyday.strip())
#input()

