from django.test import TestCase
from rest_framework.views import APIView
import json
from myblog.seriliz import pointseriliz
from myblog.models import viewpoint
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,QueryDict
# Create your tests here.


class jsonss(APIView):

#     定义get获取
    def get (self,request,*args,**kwargs):

        # 获取地址栏参数
        names=request.GET['name']
        ages=request.GET['age']

        return HttpResponse('ok')


    def post(self,request,*args,**kwargs):

        # 获取json数据

        datas= request.body.decode()
        datas=json.loads(datas)
        # print(datas['name'])


        # 查询数据库，返回json集合，可根据情况选择不同序列化器
        # datas = viewpoint.objects.all()
        #
        # dataresp = pointseriliz(datas, many=True)
        # dataresps=dataresp.data
        #


        # 自由选择数据库操作动作
        # data=viewpoint.objects.all().count()
        # # datas=pointseriliz(data,many=True)
        # # dataa=datas.data

        con={   'point':datas,
        'name':"aheeee"}



        return JsonResponse(con)





