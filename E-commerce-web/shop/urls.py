from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path("",views.index,name='shop'),
    path("about/",views.about,name='About Us'),
    path("contact/",views.contact,name='contact Us'),
    # path("tracker/",views.tracker,name='traking_status'),
    path("search/",views.search,name='serach'),
    path("checkout/",views.checkout,name='checkout'),
    path("productview/",views.productview,name='product')
]
