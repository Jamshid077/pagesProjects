from django.urls import path
from .views import HomePageView,AboutPageView,basePageViwe

urlpatterns=[
    path('home/',HomePageView.as_view(),name='home'),
    path('about/',AboutPageView.as_view(),name='about'),
    # path('sayt/',SaytPageView.as_view(),name='sayt_nomi'),
    path('',basePageViwe.as_view(),name='base'),
]