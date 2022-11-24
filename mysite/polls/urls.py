from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    #path('persons/', views.person_list),
    #path('persons/<int:pk>/', views.person_detail),
    path('teams/', views.team_list),
    path('teams/<int:pk>/', views.team_detail),
    path('persons/', views.SnippetList.as_view()),
    path('persons/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
