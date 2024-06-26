"""
URL configuration for django1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
"""
comentei agora
from django.contrib import admin
from django.urls import path
from core.views import index, contato


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('contato', contato),

]
"""

from django.contrib import admin
from django.urls import path

from core.views import index, contato, produto
from django.conf.urls import handler404, handler500

from core import views


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('contato', contato, name='contato'),
    path('produto/<int:pk>', produto, name='produto'),
]

handler404 = views.error404
handler500 = views.error500


