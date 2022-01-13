from django.shortcuts import render

from history.forms import CarrierForm
from .models import LineHistory, Carrier, Carrier_number
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

#rest_framwork api 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Carrier_number_serializer, Carrier_serializer

# Create your views here.

class Lineview(ListView):
    model = LineHistory
    template_name = 'Listhistory.html'
    context_object_name = 'history' 
    
class HistoryView(ListView):
    model = Carrier_number
    template_name = 'history.html'
    context_object_name = 'history'

class CarrierView(ListView):
    model = Carrier
    template_name = 'carrier.html'
    context_object_name = 'carrier'

    def __str__(self):
        return str(self.carrier_num)

    def get_queryset(self):
        return Carrier.objects.filter(carrier_num=self.kwargs['carrier_num'])

class CarrierCreateView(CreateView):
    model = Carrier
    form_class = CarrierForm
    template_name = 'createcarrier.html'
    success_url = reverse_lazy("history")

    # def form_valid(self, form):
    #     carrier_num = self.request.carrier_num
    #     form.instance.carrier_num = carrier_num
    #     return super(CarrierCreateView, self).form_valid(form)

@api_view(['GET'])
def carrier_number_api(request):
    carrier_num = Carrier_number.objects.all()
    serializers = Carrier_number_serializer(carrier_num, many=True)
    return Response(serializers.data)

@api_view(['GET', 'POST', 'DELETE'])
def carrier_api(request, pk):
    carrier = Carrier.objects.filter(carrier_num = pk)
    serializers = Carrier_serializer(carrier, many=True)
    return Response(serializers.data)