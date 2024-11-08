from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from .models import User, Employer, JobSeeker, JobPost, Application

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ['id', 'company_name', 'company_description']

class JobSeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeeker
        fields = ['id', 'cv']

class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = ['id', 'title', 'description', 'required_skills', 'salary_range', 'is_enabled', 'employer']

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'job_post', 'job_seeker', 'status', 'applied_at']


class UserRegistrationSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=User.ROLE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class EmployerRegistrationSerializer(serializers.ModelSerializer):
    user = UserRegistrationSerializer()


    class Meta:
        model = Employer
        fields = ['user', 'company_name', 'company_description']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = user_data.pop('password')

        # Create the user without specifying 'role'
        user = User.objects.create_user(**user_data)
        user.set_password(password)
        user.role = 'employer'  # Set role after creating the user
        user.save()

        # Create Employer instance
        return Employer.objects.create(user=user, **validated_data)
    
class JobSeekerRegistrationSerializer(serializers.ModelSerializer):
    user = UserRegistrationSerializer()

    class Meta:
        model = JobSeeker
        fields = ['user', 'cv']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data, role='job_seeker')
        return JobSeeker.objects.create(user=user, **validated_data)

class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data['role']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return {'user': user}
        raise serializers.ValidationError("Invalid login credentials.")




