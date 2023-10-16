"""THE_ELITE_5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from THE_ELITE_5.views import landing
from THE_ELITE_5.views import data
# import settings.py
# from THE_ELITE_5.views import submit_form


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", landing),
    path("data/",data,name="THE_ELITE_5\templates\data_analysis\homepage.html"),
    # path("", index,name="index.html")
    # path('submit_form/', submit_form, name='submit_form'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
