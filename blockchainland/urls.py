"""blockchainland URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from land import views

urlpatterns = [
    path('/',views.index())
    path('admin/', admin.site.urls),
    path('create/',views.CreateView.as_view()),
    path('transfer/',views.TransferView.as_view()),
    path('register/',views.RegisterView.as_view()),
    path('all_properties',views.LandListView.as_view()),
    path('generate/',views.generate),
    path('land/<int:pk>/',views.LandDetailView.as_view(), name='land_detail'),
    path('searchableselect/', include('searchableselect.urls')),
]
