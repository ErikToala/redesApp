from rest_framework import routers, serializers, viewsets

from Login.models import Login2

class Login2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Login2
        fields = ('__all__')
