from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from .models import Kroy, Kroy_detail
from .forms import KroyForm, KroyDetailForm
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse_lazy

def index(request):


    return render(request, "main/index.html")

class KroyListView(ListView):
    model = Kroy
    template_name = 'main/kroy_list.html'

def KroyCreateListView(request):

    context = {
        "kroy": Kroy.objects.all(),
    }

    return render(request, "main/kroy_form.html", context)
class KroyCreateView(CreateView):
    model = Kroy
    form_class = KroyForm
    template_name = 'main/kroy_form.html'
    success_url = '/kroy/'

def KroyDetailView(request, kroy_id):
    kroy_instance = get_object_or_404(Kroy, pk=kroy_id)
    kroy_details = Kroy_detail.objects.filter(kroy=kroy_instance)  # Retrieve related Kroy_detail records

    context = {
        'kroy_instance': kroy_instance,
        'kroy_details': kroy_details,  # Pass the related records to the template
    }
    return render(request, 'main/kroy_detail_view.html', context)
class KroyUpdateView(UpdateView):
    model = Kroy
    form_class = KroyForm
    template_name = 'main/kroy_form.html'
    success_url = '/kroy/'

class KroyDetailListView(ListView):
    model = Kroy_detail
    template_name = 'main/kroy_detail_list.html'
    verbose_name = ''

class KroyDetailCreateView(CreateView):
    model = Kroy_detail
    form_class = KroyDetailForm
    template_name = 'main/kroy_detail_form.html'
    success_url = '/kroy-detail/'

class KroyDetailUpdateView(UpdateView):
    model = Kroy_detail
    form_class = KroyDetailForm
    template_name = 'main/kroy_detail_form.html'
    success_url = '/kroy-detail/'



