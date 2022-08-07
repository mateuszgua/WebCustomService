from django.urls import path
from . import views

urlpatterns = [
    # Results in charts
    path('results/', views.results, name='results'),

]