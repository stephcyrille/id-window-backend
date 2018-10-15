from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters


from .models import PeopleEntity
from .serializer import EntityPeopleSerializer


from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework import serializers


class EntityCniUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeopleEntity
        fields = ('nberCni',)


class EntityPartialUpdateCni(GenericAPIView, UpdateModelMixin):
    '''
        You just need to provide the field which is modify
    '''
    queryset = PeopleEntity.objects.all()
    serializer_class = EntityCniUpdateSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)




class EntityStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeopleEntity
        fields = ('statut',)


class EntityPartialUpdateStatus(GenericAPIView, UpdateModelMixin):
    '''
        You just need to provide the field which is modify
    '''
    queryset = PeopleEntity.objects.all()
    serializer_class = EntityStatusUpdateSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)



class EntitiesList(APIView):
    def get (self, request, format=None):
        entities = PeopleEntity.objects.all()
        serializer = EntityPeopleSerializer(entities, many=True)
        return Response(serializer.data)

    def post (self, request, format=None):
        serializer = EntityPeopleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EntityDetail(APIView):
   
    def get(self, request, format=None):
        nberRecep = self.request.query_params.get('nberRecep', None)
        try:
            recep = PeopleEntity.objects.get(nberRecep=nberRecep)
            serialized_data = EntityPeopleSerializer(recep)
            return Response(serialized_data.data)
        except PeopleEntity.DoesNotExist:
            raise Http404



from django.db.models import Q
class EntityDistributionQueryList(ListAPIView):
    serializer_class = EntityPeopleSerializer

    def get_queryset(self):
        queryset = PeopleEntity.objects.all()
        nberRecep = self.request.query_params.get('nberRecep', None)
        if nberRecep is not None:
            queryset = queryset.filter(~Q(nberCni=None), nberRecep__startswith=nberRecep, statut='Indisponible')
        return queryset


class EntityCorrespondQueryList(ListAPIView):
    serializer_class = EntityPeopleSerializer

    def get_queryset(self):
        queryset = PeopleEntity.objects.all()
        nberRecep = self.request.query_params.get('nberRecep', None)
        if nberRecep is not None:
            queryset = queryset.filter(nberCni=None, nberRecep__startswith=nberRecep)
        return queryset


def sendSms(request, id):
    return 'OK'