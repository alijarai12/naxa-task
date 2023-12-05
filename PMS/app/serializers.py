from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'department_name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ['id', 'user', 'first_name', 'last_name', 'email']


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'owner', 'department', 'description', 'completed_status', 'project_start_date', 'project_end_date']


class UserStatsSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    month = serializers.IntegerField()
    year = serializers.IntegerField()
    project_count = serializers.IntegerField()


class AttachmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attachment
        fields = ['id', 'project', 'user', 'file_path', 'attachment_date']

