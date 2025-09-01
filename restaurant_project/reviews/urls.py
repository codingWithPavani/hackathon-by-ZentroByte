from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reviews/', views.home, name='home'),

    # Custom admin dashboard (staff only)
    path('owner-dashboard/', views.admin_page, name='admin_page'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('delete-review/<int:review_id>/', views.delete_review, name='delete_review'),
    path("resolve-review/<int:review_id>/", views.resolve_review, name="resolve_review"),
    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='reviews/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),

    path("owner/reviews/", views.admin_page, name="owner_reviews"),


]   