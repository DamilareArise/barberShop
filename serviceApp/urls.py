from django.urls import path
from .views import *

urlpatterns = [
    path('create-service/',createService, name='create-service'),
    path('all_services/', all_services, name='all_services'),
    path('service_detail/<int:serv_id>/', service_detail, name='service_detail'),
    path('edit_service/<int:serv_id>/', edit_service, name='edit_service'),
    path('delete_service/<int:serv_id>/', delete_service, name='delete_service'),
    path('creat_sub_service/<int:serv_id>/', create_subService, name='create_sub_service'),
    path('subService_detail/<int:sub_servId>/', subService_detail, name='subService_detail'),
    path('edit_subService/<int:sub_servId>/', edit_subService, name='edit_subService'),
    path('delete_subService/<int:sub_servId>/<int:serv_id>/', delete_subService, name = 'delete_subService')
]
