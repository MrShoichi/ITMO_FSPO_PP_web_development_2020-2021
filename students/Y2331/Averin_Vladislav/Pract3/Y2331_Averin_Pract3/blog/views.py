from django.shortcuts import *
from django.http import Http404
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from .forms import *
from blog.models import *
from django.contrib.auth import update_session_auth_hash
from django.template import RequestContext


def detail(request, id):
    try:
        p = CarOwner.objects.get(pk=id)
    except CarOwner.DoesNotExist:
        raise Http404("Owner does not exist")
    print(p)
    return render(request, 'Owner/detail.html', {'Owner': p})


def car_owners(request):

    context = {}

    context["dataset"] = CarOwner.objects.all()

    return render(request, "Owner/owner_list.html", context)


class CarOwnersList(ListView):
    # specify the model for list view
    model = CarOwner
    template_name = 'Owner/car_owner_ListView.html'


class CarList(ListView):
    # specify the model for list view
    model = Car
    template_name = 'Owner/car_list.html'


class ListCar(ListView):
    # specify the model for list view
    model = Car
    template_name = 'Owner/list_of_car.html'


class CarDetail(DetailView):
    model = Car
    template_name = 'Owner/CarDetail.html'


class CarUpdate(UpdateView):
    model = Car
    fields = ['state_number', 'mark', 'model', 'color']
    # form_class = CarForm
    template_name = 'Owner/Update_Car.html'
    success_url = '/CarList/'


class CarCreate(CreateView):
    model = Car
    fields = ['state_number', 'mark', 'model', 'color']
    template_name = 'Owner/create_car_owner.html'
    success_url = '/CarList/'


class CarDelete(DeleteView):
    model = Car
    template_name = 'Owner/delete_car.html'
    success_url = '/CarList/'


def register_student(request):
    context = {}
    if request.method == 'POST':
        car_owner_form = CarOwnerForm(data=request.POST)

        if car_owner_form.is_valid():
            car_owner = car_owner_form.save()
            car_owner.set_password(car_owner.password)
            car_owner.save()

    else:
        car_owner_form = CarOwnerForm()
    context['form'] = car_owner_form
    return render(request, 'Owner/create_car_owner.html', context)

