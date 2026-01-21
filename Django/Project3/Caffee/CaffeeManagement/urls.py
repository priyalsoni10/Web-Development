"""
URL configuration for Caffee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    path('getMenu/',views.getMenu),
    path('getOneItem/<int:id>',views.dishById),
    path('getItemByName/',views.dishByName),
    path('createMenu',views.createItem),
    path('updateMenu/<int:id>',views.updateItem),
    path('deleteMenu/<int:id>',views.deleteItem),
    path('makeOrder/',views.makeOrder),
    path('updateOrder/<int:id>',views.updateOrder),
    path('getBill/<int:id>/',views.getBill)
]

