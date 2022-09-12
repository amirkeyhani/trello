from django.db import models

from users.models import User
from django.utils import timezone

from django.contrib.contenttypes.fields import GenericRelation
from boards.models import Board

# Create your models here.

class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_projects')
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    members = models.ManyToManyField(
        User, through='ProjectMembership', through_fields=('project', 'member'))
    
    boards = GenericRelation(
        Board, object_id_field='owner_id', content_type_field='owner_model')
    
    def __str__(self):
        return self.title
    
class ProjectMembership(models.Model):
    class Access(models.IntegerChoices):
        MEMBER = 1
        ADMIN = 2
        
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    access_level = models.IntegerField(choices=Access.choices, default=1)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.member.full_name}, {self.project.title}'
    
    class Meta:
        unique_together = ('project', 'member')