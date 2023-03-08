from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from datetime import date
from .models import Client
from .forms import ClientFrom


# Create your views here.


def clients(request):
    if request.method == 'POST':
        form = ClientFrom(request.POST)
        if form.is_valid():
            client = Client(full_name=form.cleaned_data['full_name'],
                            gender=form.cleaned_data['gender'],
                            birth_date=form.cleaned_data['birth_date'],
                            address=form.cleaned_data['address'])
            client.save()
    else:
        form = ClientFrom()
    clients = Client.objects.all()
    total_clients = clients.count()
    return render(request, 'clients/index.html', {
        'form': form,
        'clients': clients,
        'total_clients': total_clients
    })


def new_client(request):
    # myself = Clients(full_name="Kanat Mergenbayev", gender="male", birth_date=date.today(),
    #                  address="my adress", insurance_id=123456789)
    return HttpResponse("New client")


def delete_client(request):
    return HttpResponse("Delete client")


def client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    return render(request, 'clients/client.html', {
        'full_name': client.full_name,
        'birth_date': client.birth_date,
        'gender': client.gender,
        'address': client.address,
        'insurance_id': client.insurance_id
    })
