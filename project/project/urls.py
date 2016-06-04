"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import invites.views
from django.conf.urls.static import static
import settings

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^$', invites.views.main),
                  url(r'^invites/(?P<invite>[A-Z0-9]{100})$', invites.views.invite_handler),
                  url(r'^out$', invites.views.out),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
