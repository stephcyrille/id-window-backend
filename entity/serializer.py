from rest_framework import serializers
from .models import PeopleEntity



class EntityPeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeopleEntity
        fields = ('id', 'nberCni', 'nberRecep', 'name', 'surname', 'birthdate', 'birthPlace', 'nationality', 'profession', 'phone', 'address', 'madePlace', 'statut')