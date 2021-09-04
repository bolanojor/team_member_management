from django.urls import path
from team_member import views

# List is the default view
urlpatterns = [
    path('add/', views.add, name='add'),
    path('edit/<int:team_member_id>', views.edit, name='edit'),
    path('delete/<int:team_member_id>', views.delete, name='delete'),
    path('', views.list, name='list'),
]
