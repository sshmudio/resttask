from rest_framework import serializers
from apiusers.models import Users


# class UserSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Users
#         fields = '__all__'

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

    def create(self, validated_data):
        return Users.objects.create(**validated_data)
