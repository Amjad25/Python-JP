from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import JobPost, Application
from .serializers import JobPostSerializer, ApplicationSerializer
from .permissions import IsAdminUser, IsEmployerUser, IsJobSeekerUser




@api_view(['POST'])
def signup(request):
    """
    Allows a new user to sign up.
    """
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
