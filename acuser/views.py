from django.shortcuts import render

# Create your views here.
from .models import Names, Periods
from rest_framework import viewsets
from acuser.serializers import NamesSerializer, PeriodsSerializer


class NamesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Names.objects.all()
    serializer_class = NamesSerializer


class PeriodsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Periods.objects.all()
    serializer_class = PeriodsSerializer


    