from django.urls import path,include
from . import views

app_name='fi_user'

urlpatterns = [

    path('<countryName>/', views.Fetch_detail.as_view()),
 
]