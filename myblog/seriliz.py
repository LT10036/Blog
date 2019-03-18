from rest_framework import serializers
from myblog.models import author,viewpoint,visitor,visitorhistory


class pointseriliz(serializers.ModelSerializer):

    class Meta:
        model=viewpoint
        fields='__all__'