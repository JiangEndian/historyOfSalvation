from django.http import HttpResponse
from django.shortcuts import render_to_response
 
# 表单
def search_form(request): #对此url返回网页
    return render_to_response('search_form.html')
 
# 接收请求数据
def search(request): #对此GET url处理并返回 
    request.encoding='utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)
