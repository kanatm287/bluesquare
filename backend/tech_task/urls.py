from django.urls import path
from . import views


urlpatterns = [
    path('', views.ClientsView.as_view()),
    path('delete', views.delete_client),
    path('<int:client_id>', views.client, name='client-detail')
]
