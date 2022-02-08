from polls.views import (index,update_person)
from django.urls import path
from polls.views import update_person 

urlpatterns = [
    path('', index, name = 'home'),
    path('update/<int:pk>/',
    update_person,
    name = 'update'
    )
]