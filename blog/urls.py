from django.urls import path, include, re_path
from .views import *
from rest_framework import routers
from blog.api.views import (BLogPostView, AboutView)
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('blogpost', BLogPostView)
router.register('about', AboutView)
urlpatterns = [
    path('api/', include(router.urls)),

    path('', blog_list_view, name='list'),
    path('create/', blog_create_view, name='create'),
    path('<str:slug>/', blog_detail_view, name='detail'),
    path('<str:slug>/edit/', blog_update_view),
    path('<str:slug>/delete/', blog_delete_view),

    # give the ability to login or logout you can see by writing  api-auth/login/
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', obtain_auth_token)
]
