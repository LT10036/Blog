import json
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
# Create your views here.
from myblog.seriliz import pointseriliz
from myblog.models import viewpoint,author
from rest_framework.views import APIView
import time



from rest_framework.response import Response


#   apiview  中 request 直接 data 出 全 部 请 求 体,  不用 VIEW 中 POST
class response(APIView):
    def get(self,request):
        datas = viewpoint.objects.all()
        dataresp = pointseriliz(datas, many=True)
        dataresp=dataresp.data


        # print(type(con)
        hello = request.COOKIES.get('name')





        con={
            'point':dataresp,
            'cookue':hello

        }
        return render(request,'index.html',context=con)





# 处理注册业务逻辑
def register2(request):
    # 如果是直接地址栏输入此地址，则转到首页
    if request.method=='GET':
        url=redirect('/')
        return url
    else:
        # 接收表单数据
        re=request.POST
        user=re['user']
        password=re['password']
        password2=re['password2']
        tel=re['tel']
        age=re['age']
        datatime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

        if not author.objects.filter(tel=tel).count():
            if password==password2:

                author.objects.create(name=user,tel=tel, age=age,crt_time=datatime,sex=0)


                return HttpResponse('注册成功')
        else:
            return HttpResponse('账号已存在')



        # 接收前端传入jeon数据
        # re=request.body.decode()
        #
        # ree=json.loads(re)
        # print(ree['name'],ree['age'])
        #
        # con={
        #     'name':'zhangsan'
        # }
        #
        # # 返回json数据
        # return JsonResponse(con)


# 注册页面
def register(request):

    return render(request,'registeruser.html')




def login2(request):
    if  request.method=="GET":
        url= redirect('/')
        return url
    else:

        name=request.POST['name']
        password=request.POST['password']

        if  not all([name,password]):
            return HttpResponse('用户名密码不能为空')

        else:
            if author.objects.filter(name=name).count():
                password2=author.objects.values('tel').get(name=name)
                print(password2)
                password3=password2['tel']
                if password==password3:
                    re=HttpResponse('登陆成功')
                    re.set_cookie('name',password)
                    return re

                else:
                    return HttpResponse('用户名密码错误')
            else:
                return HttpResponse('用户不存在')






def login(request):
    if request.method=='GET':
        import random
        a=random.randint(0,99999)
        b='%06d'%a
        data={
            'data':b
        }
        return render(request,'login.html',context=data)
    else:
        url=redirect('/')
        return url


