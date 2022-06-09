from django.shortcuts import render

import os
global my_dict
my_dict = {}
#碎片化复习当天内容（数据库可能重启，因此，dump）
#1、未复习且未有dump则查询好，并放到dict中dump
if os.path.exists('/home/ed/new_grace/HelloWorld/language_voice_diction_english/PlanDatabase.sqlite'):
    my_dict['showinfo'] = '检测到数据库'
#2、每次调用，读取一次dict，并相应修改一次数据库
#3、直到，查完事，结束并删除dump文件，生成已复习
def hello(request):
    global my_dict
    context = {}
    context['hello'] = my_dict['showinfo']

    #用render替代普通返回，使用字典为参数
    #context的'hello'对应模板html的变量{{ hello }}
    return render(request, 'hello.html', context)

#还需要def alt1, alt2这样的
