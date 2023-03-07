from django.http import HttpResponse
from django.shortcuts import render

from datetime import date


# Create your views here.


def clients(request):
    return HttpResponse("Clients")


def new_client(request):
    # myself = Clients(full_name="Kanat Mergenbayev", gender="male", birth_date=date.today(),
    #                  address="my adress", insurance_id=123456789)
    return HttpResponse("New client")


def delete_client(request):
    return HttpResponse("Delete client")


def client(request, client_id):
    return HttpResponse("Client " + str(client_id))
