from django.urls import path
from . import views

urlpatterns = [
    # Member views
    path('members/', views.MemberListView.as_view(), name='member-list'),
    path('members/create/', views.MemberCreateView.as_view(), name='member-create'),
    path('members/<int:pk>/', views.MemberDetailView.as_view(), name='member-detail'),
    path('members/<int:pk>/update/', views.MemberUpdateView.as_view(), name='member-update'),
    
    # Process views
    path('processes/', views.ProcessListView.as_view(), name='process-list'),
    path('processes/create/', views.ProcessCreateView.as_view(), name='process-create'),
    path('processes/<int:pk>/', views.ProcessDetailView.as_view(), name='process-detail'),
    path('processes/<int:pk>/update/', views.ProcessUpdateView.as_view(), name='process-update'),
]
