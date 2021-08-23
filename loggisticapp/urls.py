from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'', views.home, name="homepage"),
    url(r'dashboard', views.dashboard, name="dashboardpage"),
    url(r'MyShipments', views.MyShipments, name="MyShipmentspage"),
    url(r'MyConsolidations', views.MyConsolidations, name="MyConsolidationspage"),

]
