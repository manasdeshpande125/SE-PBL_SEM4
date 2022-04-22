from django.contrib import admin
from django.urls import path
from .views import SAP,Details,New,Edit,delete,CustomLoginView,RegisterPage
from django.conf import settings
from django.conf.urls import static
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',SAP.as_view(), name='SAP'),
    path('Details/<int:pk>/',Details.as_view(), name='Details'),
    path('SAP-create/',New.as_view(), name='SAP-create'),
    path('SAP-Edit/<int:pk>/',Edit.as_view(),name='SAP-Edit'),
    path('SAP-delete/<int:pk>/',delete.as_view(),name='SAP-delete'),
    path('login/',CustomLoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(next_page='login'),name="logout"),
    path('register/',RegisterPage.as_view(),name='register'),
    path('change-password/',auth_views.PasswordChangeView.as_view(template_name='CRUD/change-password.html',success_url = '/')
    ,name='change_password'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)