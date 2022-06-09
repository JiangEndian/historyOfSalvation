from django.shortcuts import render
from django.views.decorators import csrf
 
# 接收POST请求数据
def search_post(request):
    ctx ={}
    if request.POST: #如果post，则附加上请求的q
        ctx['rlt'] = request.POST['q'] #附到rlt上
        #正好网页也有个最后部分rlt来显示。。。
    return render(request, "post.html", ctx)
