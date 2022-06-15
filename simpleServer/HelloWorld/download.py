from django.http import HttpResponseRedirect 
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
import os
from MyPython3 import *
from configurations import *

global file_dict
updateTimeInfo()

def download(request):
    global file_dict
    file_list = os.listdir("statics/files")
    file_list.sort()
    file_dict['file_list'] = file_list
    allItems = len(file_list)
    halfItems = int(allItems/2)

    #尝试加个控制页面，设置显示删除与否
    Configurations = readConfigurations('Configurations')
    file_dict['Delete']= Configurations['Delete']
    file_dict['allItems'] = allItems
    file_dict['halfItems'] = halfItems

    file_dict['TextArea'] = readffile('from_net')
    if len(file_dict['TextArea']) < 5:
        runsyscmd('df -h > dfResult')
        file_dict['TextArea'] = readffile('dfResult')
    return render(request, 'download.html', file_dict)

def deleteFile(request):
    #runsyscmd('mv statics/files/%s /home/ed/DeletedFiles/' % request.GET.get('FileName').replace(' ', '\ ')) #不知道为什么，我9点多起来，6点半左右删了好几个文件。。。
    runsyscmd('date >> /home/ed/DeletedFiles/RecordsOfFileOperation; echo %s >> /home/ed/DeletedFiles/RecordsOfFileOperation; echo >> /home/ed/DeletedFiles/RecordsOfFileOperation' % request.GET.get('FileName').replace(' ', '\ '))
    #file_list = os.listdir("statics/files")
    #file_dict = {'file_list':file_list}
    #return render(request, 'download.html', file_dict) 
    #above one will keep the link with commands, 
    return HttpResponseRedirect('/alt')

def video_view(request):
    file_list = []
    for file_one in os.listdir("statics/videosView"):
        file_name_splited = os.path.splitext(file_one)
        if len(file_name_splited) > 1:
            #if file_name_splited[1] == '.mp4':
            if True:
                file_list.append(file_one)
    file_dict['file_list'] = sorted(file_list)
    return render(request, 'video_view.html', file_dict)


#试着返回JSON数据。为了以后如果扩展可以直接获取数据准备
def video_name(request):
    file_list = []
    for file_one in os.listdir("statics/videosView"):
        file_name_splited = os.path.splitext(file_one)
        if len(file_name_splited) > 1:
            if file_name_splited[1] == '.mp4':
                file_list.append(file_one)
    file_dict['file_list'] = file_list
    return JsonResponse(data=file_dict)
    #return render(request, 'video_view.html', file_dict)

def upload_file(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理
        myFiles =request.FILES.getlist("myfiles", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not myFiles:
            return HttpResponse("no files for upload!")
        for oneFile in myFiles:
            destination = open("./statics/files/" + oneFile.name, 'wb+')    # 打开特定的文件进行二进制的写操作
            for chunk in oneFile.chunks():      # 分块写入文件
                destination.write(chunk)
            destination.close()
        return HttpResponseRedirect('/alt')

def bibletimeDownload(request):
    runsyscmd('bash bibletimeCompress.bash', 'no')
    return HttpResponseRedirect('/static/grace_voice/bibletime.zip')

def age2days(request):
    info_dict = {}
    request.encoding='utf-8'
    if "name" in request.GET:
        name = request.GET['name']
    else:
        name = '耶稣复活'

    if "birthday" in request.GET:
        birthday = request.GET['birthday']
    else:
        birthday = '0032-03-02'

    if "longevity" in request.GET:
        longevity = request.GET['longevity']
    else:
        longevity = '80'

    info_dict['name'] = name
    info_dict['birthday'] = birthday
    info_dict['longevity'] = longevity

    return render(request, 'age2days.html', info_dict)

def runThoseCmds(request):
    request.encoding='utf-8'
    text = request.POST.get('cmdList', '')
    cmds = text.split('\n')
    for cmd in cmds:
        print(cmd)
        runsyscmd(cmd, 'yes')
    return HttpResponseRedirect('/configurationsWeb')

def ftpGetFrom(request):
    runsyscmd('ftp -n < /home/ed/grace_20190205/ftpGetFrom10_42_0_2_2121.ftp', 'yes')
    return HttpResponseRedirect('/configurationsWeb')

def backBT_ALL(request):
    runsyscmd('ftp -n < /home/ed/grace_20190205/BT_ALL_backTo10_42_0_2_2121.ftp', 'yes')
    return HttpResponseRedirect('/configurationsWeb')

