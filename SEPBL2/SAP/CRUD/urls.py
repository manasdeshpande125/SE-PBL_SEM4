from django.contrib import admin
from django.urls import path
from .views import SAP,Details,New,Edit,delete,CustomLoginView,RegisterPage,admin1,UserEditView,New1,Edit1,prof
from django.conf import settings
from django.conf.urls import static
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',SAP.as_view(), name='SAP'),
    path('admin1/',admin1.as_view(),name="admin1"),
    path('Details/<int:pk>/',Details.as_view(), name='Details'),
    path('SAP-create/',New.as_view(), name='SAP-create'),
    path('SAP-Edit/<int:pk>/',Edit.as_view(),name='SAP-Edit'),
    path('SAP-delete/<int:pk>/',delete.as_view(),name='SAP-delete'),
    path('login/',CustomLoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(next_page='login'),name="logout"),
    path('register/',RegisterPage.as_view(),name='register'),
    path('change-password/',auth_views.PasswordChangeView.as_view(template_name='CRUD/change-password.html',success_url = '/')
    ,name='change_password'),
    path('edit_profile',UserEditView.as_view(),name='edit_profile'),
    path('new_prof',New1.as_view(), name='new_prof'),
    path('edit_prof/<int:pk>/',Edit1.as_view(), name='edit_prof'),
    path('prof',prof.as_view(), name='prof'),
    path('group',views.group, name="group"),

]
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)