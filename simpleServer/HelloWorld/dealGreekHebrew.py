from django.http import HttpResponseRedirect 
from django.shortcuts import render

def dealGreekHebrew(request):
    request.encoding='utf-8'
    #help(request)
    #print(request)
    path = request.get_full_path()
    new_path = path.replace('hebrew', 'static/originalLang/hebrew').replace('greek', 'static/originalLang/greek')
    #print(new_path)
    return HttpResponseRedirect(new_path)

