from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView
from .models import Kroy, Kroy_detail, Uchastok
from .forms import KroyForm, KroyDetailForm, Masterdata, MasterdataSearchForm
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse_lazy
from django.db.models import Max
from django.db.models import Q

def index(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "main/index.html")

def create_masterdata(request):
    if request.method == 'POST':
        kroy_no = request.POST.get('kroy_no')
        status = request.POST.get('status')
        edinitsa = request.POST.get('edinitsa')

        try:
            edinitsa = int(edinitsa)
        except ValueError:
            edinitsa = 0  # Default value if parsing fails
        # Create a new Masterdata object and save it to the database
        masterdata = Masterdata(
            kroy_no=kroy_no,
            status=status,
            edinitsa = edinitsa
            # Add other fields here as needed
        )
        masterdata.save()

        kroy_record = get_object_or_404(Kroy, kroy_no=kroy_no)
        kroy_record.edinitsa = int(kroy_record.edinitsa or 0) - edinitsa
        kroy_record.save()

        return redirect('create_masterdata')

    return render(request, 'main/kroy/kroy_masterdata.html')

class MasterdataListView(ListView):
    model = Masterdata
    template_name = 'main/kroy/masterdata_list.html'
    context_object_name = 'masterdata_list'

    def get_queryset(self):
        form = MasterdataSearchForm(self.request.GET)
        queryset = Masterdata.objects.filter(is_active=True)

        if form.is_valid():
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            status_search = form.cleaned_data.get('status_search')
            kroy_no_search = form.cleaned_data.get('kroy_no_search')

            if start_date:
                queryset = queryset.filter(created__gte=start_date)
            if end_date:
                queryset = queryset.filter(created__lte=end_date)
            if status_search:
                queryset = queryset.filter(Q(status__icontains=status_search))
            if kroy_no_search:
                queryset = queryset.filter(Q(kroy_no__icontains=kroy_no_search))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = MasterdataSearchForm(self.request.GET)
        return context

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

class MasterdatauserListView(ListView):

    model = Masterdata
    template_name = 'main/masterdatauser_list.html'
    #context_object_name = 'index'
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        return super().dispatch(request, *args, **kwargs)

