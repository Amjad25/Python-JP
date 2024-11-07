from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom user model with roles
class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('employer', 'Employer'),
        ('job_seeker', 'Job Seeker'),
    ]
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    company_description = models.TextField(null=True, blank=True)

class JobSeeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cv = models.FileField(upload_to='emp_cvs/',null=True, blank=True)

class JobPost(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name="job_posts")
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    required_skills = models.TextField(null=True, blank=True)
    salary_range = models.CharField(max_length=100,null=True, blank=True)
    is_enabled = models.BooleanField(default=True)

class Application(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('hired', 'Hired'),
    ]
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name="applications")
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, related_name="applications")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    applied_at = models.DateTimeField(auto_now_add=True)
