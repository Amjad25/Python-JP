from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import JobPost, Application ,Employer
from .serializers import EmployerSerializer, JobPostSerializer, ApplicationSerializer, UserSignupSerializer ,UserLoginSerializer,EmployerRegistrationSerializer,JobSeekerRegistrationSerializer
from .permissions import IsAdminUser, IsEmployerUser, IsJobSeekerUser
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def employer_signup(request):
    serializer = EmployerRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Employer registered successfully."}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def job_seeker_signup(request):
    serializer = JobSeekerRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Job seeker registered successfully."}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def signup(request):
    serializer = UserSignupSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': serializer.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh0),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployerViewSet(viewsets.ModelViewSet):
    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()
    permission_classes = []



class JobPostViewSet(viewsets.ModelViewSet):
    serializer_class = JobPostSerializer
    queryset = JobPost.objects.all()
    permission_classes = [IsAuthenticated, IsEmployerUser]

    def get_queryset(self):
        if self.request.user.role == 'employer':
            return self.queryset.filter(employer=self.request.user.employer)
        return self.queryset

class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'employer':
            return self.queryset.filter(job_post__employer=user.employer)
        elif user.role == 'job_seeker':
            return self.queryset.filter(job_seeker=user.jobseeker)
        return self.queryset

    def perform_create(self, serializer):
        serializer.save(job_seeker=self.request.user.jobseeker)
