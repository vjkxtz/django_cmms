from http import HTTPStatus
from django.shortcuts import render

from history.forms import CarrierForm
from .models import LineHistory, Carrier, Carrier_number, Part, Type, Sub_type
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

#rest_framwork api 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Carrier_number_serializer, Carrier_serializer, Type_serializer, Part_serializer, Sub_type_serializer

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

@api_view(['GET', 'POST'])
def part_api(request):
    if request.method == 'GET':
        data = Part.objects.all()
        serializers = Part_serializer(data, context = {'request': request}, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = Part_serializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(status = HTTPStatus.HTTP_201_CREATED)
        
        return Response(serializers.errors, status = Response.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def part_api_detail(request, pk):
    try:
        part = Part.objects.get(pk= pk)
    except Part.DoesNotExist:
        return Response(status = Response.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = Part_serializer(part, data= request.data, context = {'request': request}, many=True)
        if serializer.is_valid():
            serializer.save()   
            return Response(status = Response.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status = Response.HTTP_400_BAD_REQUEST)  

    elif request.method == 'DELETE':
        part.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)