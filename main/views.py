from rest_framework.viewsets import ModelViewSet
from .serializers import TrainersSerializer, AbonementsSerializer, ClubsSerializer, PartnersSerializer, EquipmentsSerializer, grouptrainingSerializer
from .models import Trainers, Abonements, Clubs, Partners, Equipments, grouptraining
from rest_framework.generics import ListAPIView 
import django_filters.rest_framework
from django.db.models import Q

class TrainersViewSet(ModelViewSet):
    queryset = Trainers.objects.all()
    serializer_class = TrainersSerializer

class AbonementsViewSet(ModelViewSet):
    queryset = Abonements.objects.all()
    serializer_class = AbonementsSerializer

class ClubsViewSet(ModelViewSet):
    queryset = Clubs.objects.all()
    serializer_class = ClubsSerializer

class PartnersViewSet(ModelViewSet):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer

class EquipmentsViewSet(ModelViewSet):
    queryset = Equipments.objects.all()
    serializer_class = EquipmentsSerializer

class grouptrainingViewSet(ModelViewSet):
    queryset = grouptraining.objects.all()
    serializer_class = grouptrainingSerializer


class GetTrainersView(ListAPIView):
    queryset = Trainers.objects.all()
    serializer_class = TrainersSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name', 'age']
