from django.urls import path
from . import views



urlpatterns = [
    path("", views.store, name="store"),
    path("set_language/<str:language>/", views.set_language, name="set-language"),
    path("products/", views.products_titiz, name="products-page"),
    path("products/rorax/", views.products_rorax, name="products-rorax-page"),
    path("products/modaline/", views.products_modaline, name="products-modaline-page"),
    path("products/titiz/<int:id>/", views.product_detail_titiz, name="product-detail-titiz"),
    path("products/rorax/<str:id>/", views.product_detail_rorax, name="product-detail-rorax"),
    path("products/modeline/<str:id>/", views.product_detail_modaline, name="product-detail-modaline"),
    path("index/", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contacts/", views.contacts, name="contacts"),
    path("services/", views.services, name="services"),
]
