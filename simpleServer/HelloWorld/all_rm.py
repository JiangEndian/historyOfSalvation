from tableDefine import * #导入自定义的东西
from django.http import HttpResponseRedirect 
from django.shortcuts import render
from configurations import *

def all_rm(request):
    runsyscmd('rm new_gs/4web_restudy/*')
    runsyscmd('rm language_voice_diction_english/4web_restudy/*')
    runsyscmd('rm language_voice_diction_hebrew/4web_restudy/*')
    runsyscmd('rm language_voice_diction_korean/4web_restudy/*')
    runsyscmd('rm WorshipAndBible/4web_restudy/*')
    
    runsyscmd('rm language_voice_diction_mother/4web_restudy/*') #今天为妈妈做了个学英语的，每天给妈妈加一课新的

    runsyscmd('rm file_name_files/*') #加上删除所有已完成的记录,20201207,22:51

    return HttpResponseRedirect('/alt1234')

def life_code(request):
    return render(request, 'life_code.html')

def addTask(request):
    request.encoding='utf-8'
    if 'TaskName' in request.GET:
        TaskName = request.GET['TaskName']
        if TaskName == '':
            return HttpResponseRedirect('/alt1234')
        print('NewTask:', TaskName)
        Conf = readConfigurations('Con4Task')
        if 'Tasks' in Conf:
            Tasks = Conf['Tasks']
            print('OldTasks:', Tasks)
            Tasks.append(TaskName) #神奇的，之前为NewTasks = ---，原来append不返回，直接修改原列表的。
            print('NewTasks:', Tasks)
            updateConfigurations('Con4Task', Conf, {'Tasks':Tasks})
        else:
            Tasks = list(TaskName)
            updateConfigurations('Con4Task', Conf, {'Tasks':Tasks})

    return HttpResponseRedirect('/alt1234')


def delTask(request):
    #request.encoding='utf-8'
    print(request)
    if request.method=="POST":
        TaskName = request.POST.getlist('TaskName')
        print('delTask:', TaskName)

        Conf = readConfigurations('Con4Task')
        if 'Tasks' in Conf:
            Tasks = Conf['Tasks']
            print('OldTasks:', Tasks)
            for Task in TaskName:
                Tasks.remove(Task) #神奇的，之前为NewTasks = ---，原来append不返回，直接修改原列表的。
                runsyscmd('date  >> ~/TasksDeleted.txt' )
                runsyscmd('echo %s  >> ~/TasksDeleted.txt' % Task)
            print('NewTasks:', Tasks)
            updateConfigurations('Con4Task', Conf, {'Tasks':Tasks})

    return HttpResponseRedirect('/alt1234')
