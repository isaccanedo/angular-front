from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Usuario
		fields = ['id', 'username', 'password', 'name', 'email']

	def create(self, validated_data):
		return Usuario.objects.create(
				username = validated_data['username'],
				password = make_password(validated_data['password']),
				name = validated_data['name'],
				email = validated_data['email']
			)