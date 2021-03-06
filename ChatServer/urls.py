"""ChatServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from accounts import views as account_views
from chat import views as chat_views

urlpatterns = [
    path('', include('Root.urls')),
    path('admin/', admin.site.urls),
    path('signup/', account_views.signup_view, name='signup'),
    path('login/', account_views.login_view, name='login'),
    path('logout/', account_views.logout_view, name='logout'),
    path('groups/', chat_views.groups, name='groups'),
    path('<str:grp_name>/', chat_views.selected_group, name='selected_group'),
    path('<str:grp_name>/members/', chat_views.group_members, name='group_members'),
    path('chat/', include('chat.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)