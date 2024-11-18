from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('signout/', views.signout_view, name='signout'),
    path('user_complaints/', views.user_complaints, name='user_complaints'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('update_complaint_status/<int:complaint_id>/<str:new_status>/', views.update_complaint_status, name='update_complaint_status'),
    path('add_feedback/<int:complaint_id>/', views.add_feedback, name='add_feedback'),
]
