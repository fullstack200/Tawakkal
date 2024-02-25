from django.urls import path
from .views import *

urlpatterns = [
    path('residentialMenu', residentialMenuView, name = 'residentialMenu'),
    path('commercialMenu', commercialMenuView, name = 'commercialMenu'),
    path('ongoingMenu', onGoingMenuView, name = 'ongoingMenu'),
    path('property/<uuid:id>',detailView,name = 'property'),    
    ]
