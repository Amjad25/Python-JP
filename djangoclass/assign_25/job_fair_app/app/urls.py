from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployerViewSet, JobPostViewSet, ApplicationViewSet ,signup,login,employer_signup,job_seeker_signup
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('employers', EmployerViewSet, basename='employers')
router.register('jobposts', JobPostViewSet, basename='jobpost')
router.register('applications', ApplicationViewSet, basename='application')

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('employer/signup/', employer_signup, name='employer_signup'),
    path('jobseeker/signup/', job_seeker_signup, name='job_seeker_signup'),
]+ router.urls
