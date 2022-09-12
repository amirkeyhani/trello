from django.urls import path

from .views import BoardList, BoardDetail, BoardStar, ItemList, ItemDetail, ListShow, ListDetail, LabelList, LabelDetail, CommentList, CommentDetail, AttachmentList, AttachmentDetail

urlpatterns = [
    path('', BoardList.as_view()), 
    path('<int:pk>/', BoardDetail.as_view()), 
    
    path('star/', BoardStar.as_view()), 
    
    path('items/', ItemList.as_view()), 
    path('items/<int:pk>/', ItemDetail.as_view()), 
    
    path('lists/', ListShow.as_view()), 
    path('lists/<int:pk>/', ListDetail.as_view()), 
    
    path('labels/', LabelList.as_view()), 
    path('labels/<int:pk>/', LabelDetail.as_view()), 
    
    path('comments/', CommentList.as_view()), 
    path('comments/<int:pk>/', CommentDetail.as_view()), 
    
    path('attachments/', AttachmentList.as_view()), 
    path('attachments/<int:pk>/', AttachmentDetail.as_view()), 
]
