from django.urls import path
from . import views

app_name = 'parts_of_computer_app'


urlpatterns = [
    path("", views.home_view, name="home"),
    path("anakart/", views.anakart_view, name="anakart"),
    path("ram/", views.ram_view, name="ram"),
    path("ekran-karti/", views.ekran_karti_view, name="ekran-karti"),
    path("islemci/", views.islemci_view, name="islemci"),
    path("bilgisayar-kasalari/", views.bilgisayar_kasalari_view, name="bilgisayar-kasalari"),

]