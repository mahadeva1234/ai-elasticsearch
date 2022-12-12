from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('e_search/<keyword>', views.e_search_view, name='e_search'),
]


