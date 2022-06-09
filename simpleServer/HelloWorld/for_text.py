from django.http import HttpResponseRedirect 
from django.shortcuts import render

from tableDefine import * #导入自定义的东西


def accept_text(request):
    #text = request.GET['text'] 
    text = request.POST.get('TextArea', '')
    #runsyscmd('echo %s >> from_net' % text)

    #在覆盖写入之前，把之前的文件复制到主文件夹的back4from_net里去
    BackFileName = getnowtime('ymdhms')
    runsyscmd('cp from_net /home/ed/back4from_net/%s' % BackFileName)
    write2file('from_net', text)
    return HttpResponseRedirect('/alt')

