from django.urls import path
from .views import Lineview, HistoryView, CarrierView, CarrierCreateView, carrier_api, carrier_number_api

urlpatterns = [
    path('', Lineview.as_view(), name='history'),
    path('list/<str:line>/', HistoryView.as_view(), name='historyview'),
    path('list/<int:carrier_num>', CarrierView.as_view(), name='carrier'),
    path('list/add/<int:carrier_num>', CarrierCreateView.as_view(), name='addcarrier'),
    path('list/api/carrier_num', carrier_number_api, name='carrier_num_api'),
    path('list/api/carrier/<int:pk>', carrier_api, name='carrier_api'),

]