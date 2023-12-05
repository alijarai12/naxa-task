from django.urls import path
from .views import *


urlpatterns = [
    

    path('userlist/', UserList.as_view(), name='blog'),


    path('departmentlist/', DepartmentList.as_view(), name='departmentlist'),

    path('department/<int:pk>/', DepartmentDetail.as_view(), name='department'),


    path('profilelist/', ProfileList.as_view(), name='profilelist'),

    path('profile/<int:pk>/', ProfileDetail.as_view(), name='profile'),


    path('count-project/', CountProject.as_view(), name='project'),
    # path('count/', Count.as_view(), name='count'),
    

    # path('user-stats/', UserStatsAPIView.as_view(), name='user-stats'),

    
    path('projectlist/', ProjectList.as_view(), name='projectlist'),

    path('project/<int:pk>/', ProjectDetail.as_view(), name='project'),


    path('attachmentlist/', AttachmentList.as_view(), name='attachmentlist'),

    path('attachment/<int:pk>/', AttachmentDetail.as_view(), name='attachment'),


    path('attachment-datefilter/', AttachmentListView.as_view(), name='attachment-datefilter'),



]

