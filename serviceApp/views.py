from django.shortcuts import render, get_object_or_404, redirect
from .models import Service, SubService
from django.contrib.auth.decorators import login_required
from .forms import ServiceForm, SubServiceForm
from django.contrib import messages

# Create your views here.

def index(request):
    services = Service.objects.all()
    first3_service = services[:3]
    return render(request, 'index.html', context={'services':first3_service})


@login_required
def createService(request):
    if request.method == 'POST':
        service_form = ServiceForm(request.POST, request.FILES )
        if service_form.is_valid():
            service_form.save()
        return index(request)
    else:
        service_form = ServiceForm()
        return render(request, 'serviceApp/create_service.html', {'serviceForm': service_form})
    

@login_required
def all_services(request):
    services = Service.objects.all()
    return render(request, 'serviceApp/service.html', {'services': services})

@login_required
def service_detail(request, serv_id):
    service = get_object_or_404(Service, service_id = serv_id)
    sub_services = SubService.objects.filter(service = service)
    return render(request, 'serviceApp/service_detail.html', {'service': service, 'sub_services':sub_services})

@login_required
def edit_service(request, serv_id):
    service = get_object_or_404(Service, service_id = serv_id)
    if request.method == 'POST':
        service_form = ServiceForm(request.POST or None, request.FILES or None, instance=service)

        if service_form.is_valid():
            service_form.save()
            
            messages.success(request, 'Service was successfully updated!')
            return service_detail(request, serv_id)
        else:
            messages.error(request, 'Please correct the error below.')
            return redirect('edit_service', serv_id)
    else:
        service_form = ServiceForm(instance=service)
        return render(request, 'serviceApp/edit_service.html', {'service_form': service_form})


@login_required
def delete_service(request, serv_id):
    try:
        Service.objects.get(service_id = serv_id).delete()
        messages.success(request, 'Service deleted successfully')
    except:
        messages.error(request, 'Something went wrong')
        return redirect('all_services')
    return redirect('all_services')

@login_required
def create_subService(request, serv_id):
    service = get_object_or_404(Service, service_id = serv_id)
    if request.method == 'POST':
        sub_service_form = SubServiceForm(request.POST, request.FILES )
        if sub_service_form.is_valid():
           form =  sub_service_form.save(commit=False)
           form.service = service
           form.save()
           messages.success(request, 'Sub Service was successfully created!')
        return service_detail(request, serv_id)
    else:
        sub_service_form = SubServiceForm()
        return render(request, 'serviceApp/create_SubService.html', {'subServiceForm': sub_service_form})
    