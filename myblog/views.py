import json
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
# Create your views here.
from myblog.seriliz import pointseriliz
from myblog.models import viewpoint
from rest_framework.views import APIView



from rest_framework.response import Response


#   apiview  中 request 直接 data 出 全 部 请 求 体,  不用 VIEW 中 POST
class response(APIView):
    def get(self,request):
        datas = viewpoint.objects.all()
        dataresp = pointseriliz(datas, many=True)
        dataresp=dataresp.data
        con={
            'point':dataresp
        }
        # print(type(con))
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
        print(re['user'])

        # 接收前端传入jeon数据
        # re=request.body.decode()
        #
        # ree=json.loads(re)
        # print(ree['name'],ree['age'])

        con={
            'name':'zhangsan'
        }

        # 返回json数据
        return JsonResponse(con)


# 注册页面
def register(request):

    return render(request,'registeruser.html')




