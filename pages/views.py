from django.shortcuts import render
from django.views.generic import ListView

from listings.choices import price_choices, bedroom_choices, state_choices

from listings.models import Listing
from realtors.models import Realtor


class Index(ListView):
    model = Listing
    context_object_name = "listings"
    template_name = 'pages/index.html'

    def get_queryset(self):
        return Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['state_choices'] = state_choices
        context['bedroom_choices'] = bedroom_choices
        context['price_choices'] = price_choices
        return context


class About(ListView):
    model = Realtor
    context_object_name = "realtors"
    template_name = 'pages/about.html'

    def get_queryset(self):
        return Realtor.objects.order_by('-hire_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mvp_realtors'] = Realtor.objects.all().filter(is_mvp=True)
        return context

# def index(request):
#     listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
#     context = {
#         'listings': listings,
#         'state_choices': state_choices,
#         'bedroom_choices': bedroom_choices,
#         'price_choices': price_choices
#     }
#     return render(request, 'pages/index.html', context)


# def about(request):
#     realtors = Realtor.objects.order_by('-hire_date')
#
#     mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
#
#     context = {
#         'realtors': realtors,
#         'mvp_realtors': mvp_realtors
#     }
#
#     return render(request, 'pages/about.html', context)
