from django.urls import path

from .views import ProjectList, ProjectDetail, ProjectMemberList, ProjectMemberDetail, SendProjectInvite, AcceptProjectInvite

urlpatterns = [
    path('', ProjectList.as_view()), 
    path('<int:pk>/', ProjectDetail.as_view()), 
    
    path('<int:pk>/members/', ProjectMemberList.as_view()), 
    path('members/<int:pk>/', ProjectMemberDetail.as_view()), 
    
    path('<int:pk>/invite/', SendProjectInvite.as_view()), 
    path('join/<str:token>/', AcceptProjectInvite.as_view()), 
]
