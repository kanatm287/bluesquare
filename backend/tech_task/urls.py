from django.urls import path
from . import views


urlpatterns = [
    path('', views.ClientsView.as_view(), name='clients'),
    path('delete/<int:client_id>', views.ClientDeleteView.as_view()),
    path('<int:client_id>', views.ClientView.as_view(), name='client-detail'),
    path('insurance/new', views.InsuranceView.as_view()),
    path('insurance/delete/<int:insurance_id>', views.InsuranceDeleteView.as_view())

]
