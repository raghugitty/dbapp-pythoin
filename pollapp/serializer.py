from rest_framework import serializers  
from .models import pollvoters
#from .models import person
  
class PollSerializer(serializers.ModelSerializer):
    class Meta:  
        model = pollvoters  
        fields = '__all__'


# class newusers(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
#     def update(self, instance, data):
#         instance.set_password(data.get("password"))
#         instance.save()
#         instance.refresh_from_db()
#         return instance
# class PersonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = person
#         fields = ('age', 'bio')

# class UserSerializer(serializers.ModelSerializer):
#     # person = PersonSerializer()
#     class Meta:
#         model = person
#         fields = ('id', 'username', 'password')
#         extra_kwargs = {'password': {'write_only': True, 'required': True}}

#     def create(self, validated_data):
#         person_data = validated_data.pop("person")
#         user = User.objects.create_use