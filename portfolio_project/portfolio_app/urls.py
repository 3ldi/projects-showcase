from django.urls import path
from . import views

urlpatterns = [
    # List all projects
    path('', views.index, name='index'),

    # Update a project
    path('update/<int:project_id>/', views.update_project, name="update_project"),

    # Delete a project
    path('delete/<int:project_id>/', views.delete_project, name="delete_project"),

    # Create a new project
    path('new_project/', views.new_project, name='new_project'),

    # List all messages
    path('messages', views.messages_all, name="usermsgs"),

    # Delete a message
    path('messages/delete/<int:message_id>/', views.delete_message, name="delete_message"),

    # Login, Logout and Signup paths
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
]
