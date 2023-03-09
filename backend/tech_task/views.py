from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import Client, Insurance
from .forms import ClientForm, InsuranceForm


# Create your views here.
class ClientsView(View):
    def get(self, request):
        form = ClientForm()
        clients = Client.objects.all()
        total_clients = clients.count()
        return render(request, 'clients/index.html', {
            'form': form,
            'clients': clients,
            'total_clients': total_clients
        })

    def post(self, request):
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
        clients = Client.objects.all()
        total_clients = clients.count()
        return render(request, 'clients/index.html', {
            'form': form,
            'clients': clients,
            'total_clients': total_clients
        })


class ClientDeleteView(View):
    def post(self, request, *args, **kwargs):
        client_id = kwargs['client_id']
        client = get_object_or_404(Client, pk=client_id)
        client.delete()
        return redirect('clients')


class ClientView(View):
    def get(self, request, *args, **kwargs):
        form = InsuranceForm()
        client_id = kwargs['client_id']
        form.fields["client"].initial = client_id
        client = get_object_or_404(Client, pk=client_id)
        insurances = Insurance.objects.filter(client_id=client_id)
        total_insurances = insurances.count()
        return render(request, 'clients/client.html', {
            'form': form,
            'client': client,
            'insurances': insurances,
            'total_insurances': total_insurances
        })


class InsuranceView(View):
    def post(self, request):
        form = InsuranceForm(request.POST)
        if form.is_valid():
            form.save()
            client_id = form.cleaned_data['client'].id
            return redirect('client-detail', client_id=client_id)


class InsuranceDeleteView(View):
    def post(self, request, *args, **kwargs):
        insurance_id = kwargs['insurance_id']
        insurance = get_object_or_404(Insurance, pk=insurance_id)
        client_id = getattr(insurance, 'client_id')
        insurance.delete()
        return redirect('client-detail', client_id=client_id)
