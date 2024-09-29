from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('vehicles/', views.home, name='vehicles'),
    path('vehicles/<int:id>/', views.home, name='vehicle'),
    path('vehicles/<int:id>/edit/', views.home, name='edit_vehicle'),
    path('vehicles/<int:id>/delete/', views.home, name='delete_vehicle'),
    path('vehicles/add/', views.home, name='add_vehicle'),
    path('vehicles/search/', views.home, name='search_vehicle'),
    path('vehicles/search/results/', views.home, name='search_results'),
    path('all_cars/', views.home, name='all_cars'),
    path('featured_cars/', views.home, name='featured_cars'),
    path('about/', views.home, name='about'),
    path('contact/', views.home, name='contact'),
    path('team/', views.home, name='team'),
    path('blog/', views.home, name='blog'),
    path('testimonials/', views.home, name='testimonials'),
    path('faq/', views.home, name='faq'),
    path('terms/', views.home, name='terms'),
    path('submit/', views.submit_form, name='submit_form'),  # Corrected this line
]
