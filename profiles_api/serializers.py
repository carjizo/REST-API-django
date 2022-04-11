from rest_framework import serializers

from profiles_api import models


class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializa objeto de perfil de usuario """

    class Meta:
        model = models.UserProfile
        fields = ('id','email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """ Creaturn y rretornar nuevo usuario """
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user


class CourseSerializer(serializers.ModelSerializer):
    """ Serializador para objeto de curso """
    class Meta:
        model = models.Course
        fields = ('id', 'name', 'teacher', 'duration')
        read_only_Fields = ('id',)

class RegistrationSerializer(serializers.ModelSerializer):
    """ Serializador para objeto Matricula"""
    student = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=models.UserProfile.objects.all()
    )
    course = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=models.Course.objects.all()
    )
    class Meta:
        model = models.Registration
        fields = ('id', 'student', 'course')
        read_only_Fields = ('id',)



class FatherFamilySerializer(serializers.ModelSerializer):
    """ Serializador para objeto Padre de familia"""
    student = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=models.UserProfile.objects.all()
    )
    class Meta:
        model = models.FatherFamily
        fields = ('id', 'dni', 'surnames', 'names', 'birth_date', 'sexo', 'student')
        read_only_Fields = ('id',)



class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializador de profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}