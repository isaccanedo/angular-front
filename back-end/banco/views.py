from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Usuario
from .serializers import UsuarioSerializer

#Essa visualização se encarrega da criação do usuário
class UsuarioViewSet(viewsets.ModelViewSet):
	queryset = Usuario.objects.all()
	serializer_class = UsuarioSerializer
	lookup_field = "id"

#Essa classe verifica se o usuario já existe no banco de dados do projeto
class UsuarioExiste(APIView):
	#Deixa a visualização privada (Acessivel penas com o TOKEN JWT)
	permission_classes = (IsAuthenticated,)

	def get(self, request, usuario):
		#Faz a consulta no banco para verificar o usuario
		if (len(Usuario.objects.filter(username=usuario)) > 0):
			return JsonResponse({"usuarioExiste": True}, status=200)
		else:
			return JsonResponse({"usuarioExiste": False}, status=400)