from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView

from .models import Client
from .forms import ClientFrom


# Create your views here.
class ClientsView(View):
    def get(self, request):
        form = ClientFrom()
        clients = Client.objects.all()
        total_clients = clients.count()
        return render(request, 'clients/index.html', {
            'form': form,
            'clients': clients,
            'total_clients': total_clients
        })

    def post(self, request):
        form = ClientFrom(request.POST)
        if form.is_valid():
            form.save()
        clients = Client.objects.all()
        total_clients = clients.count()
        return render(request, 'clients/index.html', {
            'form': form,
            'clients': clients,
            'total_clients': total_clients
        })


def delete_client(request):
    return HttpResponse("Delete client")


class ClientView(TemplateView):
    template_name = "clients/client.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_id = kwargs['client_id']
        selected_client = get_object_or_404(Client, pk=client_id)
        context['client'] = selected_client
        return context


# def client(request, client_id):
#     client = get_object_or_404(Client, pk=client_id)
#     return render(request, 'clients/client.html', {
#         'full_name': client.full_name,
#         'birth_date': client.birth_date,
#         'gender': client.gender,
#         'address': client.address,
#         'insurance_id': client.insurance_id
#     })
