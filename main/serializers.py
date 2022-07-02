from rest_framework.serializers import ModelSerializer
from .models import Abonements, Trainers, Clubs, Partners, grouptraining,Equipments

class TrainersSerializer(ModelSerializer):
    class Meta:
        model = Trainers
        fields = '__all__'

class AbonementsSerializer(ModelSerializer):
    class Meta:
        model = Abonements
        fields = '__all__'

class ClubsSerializer(ModelSerializer):
    class Meta:
        model = Clubs
        fields = '__all__'

class EquipmentsSerializer(ModelSerializer):
    class Meta:
        model = Equipments
        fields = '__all__'

class PartnersSerializer(ModelSerializer):
    class Meta:
        model = Partners
        fields = '__all__'

class grouptrainingSerializer(ModelSerializer):
    class Meta:
        model = grouptraining
        fields = '__all__'

