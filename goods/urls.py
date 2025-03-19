from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path("products/", views.products, name="products"),
    path("womens/", views.womens, name="womens"),
]
