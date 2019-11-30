from rest_framework import serializers

from app.models import Pregunta

from app.models import Respuesta


class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = ['id','texto','img']

class RespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respuesta
        fields = ['id','texto','votos']