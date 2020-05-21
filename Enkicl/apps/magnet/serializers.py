from rest_framework import serializers

from apps.magnet.models import Magnet

class MagnetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Magnet
        fields = "__all__"