from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView
from .models import Kroy, Kroy_detail, Uchastok
from .forms import KroyForm, KroyDetailForm, Masterdata
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse_lazy

def index(request):


    return render(request, "main/index.html")


def create_masterdata(request):
    if request.method == 'POST':
        kroy_no = request.POST.get('kroy_no')
        status = request.POST.get('status')
        edinitsa = request.POST.get('edinitsa')
        # Create a new Masterdata object and save it to the database
        masterdata = Masterdata(
            kroy_no=kroy_no,
            status=status,
            edinitsa = edinitsa
            # Add other fields here as needed
        )
        masterdata.save()

    return render(request, 'main/kroy/kroy_masterdata.html')

class KroyListView(ListView):
    model = Kroy
    template_name = 'main/kroy/kroy_list.html'
    def get_queryset(self):
        # Filter the Kroy objects where is_active is True
        return Kroy.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['uchastok'] = Uchastok.objects.all()
        return context

class KroyCreateView(CreateView):
    model = Kroy
    form_class = KroyForm
    template_name = 'main/kroy/kroy_form.html'
    success_url = '/kroy/'

def KroyDetailView(request, kroy_id):
    kroy_instance = get_object_or_404(Kroy, pk=kroy_id)
    kroy_details = Kroy_detail.objects.filter(kroy=kroy_instance)  # Retrieve related Kroy_detail records

    context = {
        'kroy_instance': kroy_instance,
        'kroy_details': kroy_details,  # Pass the related records to the template
    }
    return render(request, 'main/kroy/kroy_detail_view.html', context)
class KroyUpdateView(UpdateView):
    model = Kroy
    form_class = KroyForm
    template_name = 'main/kroy/kroy_form.html'
    success_url = '/kroy/'

class KroyDetailListView(ListView):
    model = Kroy_detail
    template_name = 'main/kroy/kroy_detail_list.html'
    verbose_name = ''

class KroyDetailCreateView(CreateView):
    model = Kroy_detail
    form_class = KroyDetailForm
    template_name = 'main/kroy/kroy_detail_form.html'
    success_url = '/kroy-detail/'

class KroyDetailUpdateView(UpdateView):
    model = Kroy_detail
    form_class = KroyDetailForm
    template_name = 'main/kroy/kroy_detail_form.html'
    success_url = '/kroy-detail/'



