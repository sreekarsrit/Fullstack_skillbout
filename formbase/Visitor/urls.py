"""
URL configuration for formbase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path
from . import views

urlpatterns = [
    path('',views.visitor_list_view,name='visitor-list'),
    path('add/',views.visitor_form_view,name='visitor-form'),
    path('views/',views.visitor_list_view,name='visitor-list'),
    path('edit/<int:id>',views.visitor_edit_view,name='visitor-edit'),
    path('delete/<int:id>',views.visitor_delete_view,name='visitor-delete'),
    ]
