from django.urls import path, include
from. import views

urlpatterns = [
    path('accounts/', views.AccountViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('accounts/<int:pk>/', views.AccountViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('transfers/', views.TransferViewSet.as_view({'post': 'create'})),
    path('auth/login/', views.AuthViewSet.as_view({'post': 'login'})),
]