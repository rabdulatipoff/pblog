from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth.views import LoginView
from . import views, forms

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('user/<str:username>/', views.post_wall, name='post_wall'),

    path('login/', LoginView.as_view(template_name = 'app/login_form.html', authentication_form = forms.LoginForm), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
