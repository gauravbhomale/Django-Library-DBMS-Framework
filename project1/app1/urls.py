from django.urls import path
from . import views

urlpatterns=[
    path('v1/',views.bookView,name='add_url'),
    path('v2/',views.showBook,name ='show_url'),
    path('v3/<int:pk>/',views.updateOrder,name='update_url'),
    path('v4/<int:pk>/',views.deleteOrder,name= 'delete_url')
]