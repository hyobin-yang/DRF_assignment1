from rest_framework import serializers
from .models import CustomUser

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'nickname', 'university']

# {
# "username" : "hb",
# "password" : "1234",
# "nickname" : "아기사자",
# "university" : "hufs"
# }

# {
# "username" : "hb2",
# "password" : "1234",
# "nickname" : "likelion",
# "university" : "hufs"
# }

# {
# "username" : "kitten",
# "password" : "1234",
# "nickname" : "야옹이",
# "university" : "YONSEI"
# }

# {
# "username" : "singularity",
# "password" : "1234",
# "nickname" : "뚜뚜",
# "university" : "YONSEI"
# }