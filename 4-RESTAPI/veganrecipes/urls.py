"""veganrecipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from veganrecipes import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipes/', views.recipes_list),
    path('recipes/<int:id>', views.recipe_detail),
]

# allows json to be displayed in the browser in case the link in the URL bar is something like http://127.0.0.1:8000/recipes.json or http://127.0.0.1:8000/2.json
urlpatterns = format_suffix_patterns(urlpatterns)

