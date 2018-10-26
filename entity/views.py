from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response



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


from entity.sms import Sms
import requests
import json




def sendMsg(request):
    # newSms = Sms.Sms()

    # sender = 'tel:+237693458540'
    # receiver = 'tel:+237693458540'
    # message = 'Bonjour, votre carte nationale d\'identité est disponible au commissariat du 11e arrondissement à Odza. \n\n@Id-found Cameroun - 2018'

    # newSms.sendSMS(sender, receiver, message, senderName='DGSN')

    ###############################################

    ##   ETECH KEYS NG - SMS Gateway Python example   ##

    ###############################################



    import urllib.parse as parser
    import urllib.request as reque



    ###############################################

    ###            ETECH KEYS NG informations        ###

    ###############################################



    host = "https://sms.etech-keys.com/ss/api.php?"

    login = "693458540"

    password = "et9t459"

    sender_id = "stephane"

    destinataire = "693458540"

    message_body = "Hello World from Python"



    ###############################################

    ### Putting together the final HTTP Request ###

    ###############################################



    http_req = host

    http_req += "login="

    http_req += parser.quote(login)

    http_req += "&password="

    http_req += parser.quote(password)

    http_req += "&sender_id="

    http_req += parser.quote(sender_id)

    http_req += "&destinataire="

    http_req += parser.quote(destinataire)

    http_req += "&message="

    http_req += parser.quote(message_body)



    ################################################

    ####            Sending the message          ###

    ################################################

    get = reque.urlopen(http_req)

    req = get.read()

    get.close()

    return req