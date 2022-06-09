#!/usr/bin/env python3

from MyPython3 import *


##################表定义#####################
tableCommon = OrderedDict()
tableCommon['ID'] = PrimaryField('id')
tableCommon['Name'] = StringField('Chinese_name') #日期
tableCommon['Money'] = StringField('money') #计划内容
tableCommon['Money_usage'] = StringField('money_usage') #计划内容
tableCommon['Time'] = StringField('time') #计划内容
tableCommon['Time_usage'] = StringField('time_usage') #计划内容
tableCommon['Other1'] = StringField('other1') #背景
tableCommon['Other2'] = StringField('other2') #补充们
tableCommon['Other3'] = StringField('other3') #次数加上

