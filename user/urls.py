from django.urls import path
from .views import *

urlpatterns = [
    path('', homepageView, name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('contact', ContactView.as_view(), name='contact'),
    path('scope', ScopeView.as_view(), name='scope'),
    path('hiw', HowItWorks.as_view(), name='hiw'),
]



