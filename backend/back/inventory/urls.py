from django.urls import path
from .views import ProductView

urlpatterns=[
    path('productos/', ProductView.as_view(), name='products_list'),
    path('productos/<int:id>', ProductView.as_view(), name='products_process')
]