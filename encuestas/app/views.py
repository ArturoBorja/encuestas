from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView

from app.models import Pregunta
from app.serializers import PreguntaSerializer

from app.serializers import RespuestaSerializer

from app.models import Respuesta
from rest_framework.response import Response
from rest_framework.views import APIView


class ListarPreguntas(ListAPIView):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer

class ListarRespuestas(ListAPIView):
    serializer_class = RespuestaSerializer
    def get_queryset(self):
        preguntaid = self.kwargs['pregunta']
        p = Pregunta.objects.get(id=preguntaid)
        return Respuesta.objects.filter(pregunta=p)

class DarVotoRespuesta(APIView):
    def get(self, request, *args, **kwargs):
        respuestaid = self.kwargs['respuesta']
        r = Respuesta.objects.get(id=respuestaid)
        r.votos = r.votos + 1
        r.save()
        serializer = RespuestaSerializer(r)
        return Response(serializer.data)