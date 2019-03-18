from rest_framework import serializers
from myblog.models import author,viewpoint,visitor,visitorhistory


class pointseriliz(serializers.ModelSerializer):

    class Meta:
        model=viewpoint
        fields='__all__'

        # 序列化指定字段，定制前端返回数据数目
        # fields =('theme','content')
