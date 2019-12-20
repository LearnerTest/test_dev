from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
    name = request.GET.get("code","")
    return render(request,"index.html",{"name":name})

def index(request):
    if request.method == "GET":
        return render(request,"index.html")
    else:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if username == "" or password == "":
            # return HttpResponse("请输入用户名或密码")
            return render(request, "index.html", {"error": "请输入用户名或密码"})
        elif username != "tom" or password != "123":
            return render(request, "index.html", {"error": "请输入正确的用户名或密码"})
        else:
            return HttpResponse("测试成功")


