
"""
URL configuration for AvtoMarketWeb project.

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
from django.contrib import admin
from django.urls import path

from apps.views import AvtoMarketViwe

urlpatterns = [
    path('' ,AvtoMarketViwe.as_view() , name='home')
]

#
# class AlijahonHomeView(ListView):
#     model = Category
#     template_name = 'home.html'
#     context_object_name = 'cate'
#
#     def get(self, request, *args, **kwargs):
#         ref_id = request.GET.get('id') or request.GET.get('referal')
#         if ref_id:
#             request.session['join_referal_id'] = ref_id
#             request.session['referrer_id'] = ref_id
#         return super().get(request, *args, **kwargs)
