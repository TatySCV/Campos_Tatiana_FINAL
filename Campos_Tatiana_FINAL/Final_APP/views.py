from django.shortcuts import render, redirect
from Final_APP.models import Participantes, Institucion, Autor
from Final_APP.forms import FormParticipantes, FormInstitucion
from Final_APP.serializers import AutorSerial, ParticipanteSerial, InstitucionSerial
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404


# Create your views here.
def index(request):
    data = {"id": "20.733.436-7", "nombre": "Tatiana Campos", "correo": "tatiana.campos03@inacapmail.cl", "carrera": "Ingeniería en informática - 2023"}
    return render(request, 'index.html', data)

def listadoParticipante(request):
    participantes = Participantes.objects.all()
    data = {'participante': participantes}
    return render(request, 'participante.html', data)

def agregarParticipante(request):
    form = FormParticipantes()

    if request.method == 'POST':
        form = FormParticipantes(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/participantes')

    data = {'form': form}
    return render(request, 'agregarParticipantes.html', data)

def agregarInstitucion(request):
    form = FormInstitucion()

    if request.method == 'POST':
        form = FormInstitucion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/participantes')

    data = {'form': form}
    return render(request, 'agregarInstitucion.html', data)

def eliminarParticipante(request, IN_id):
    participante = Participantes.objects.get(id = IN_id)
    participante.delete()
    return redirect('/participantes')

def modificarParticipante(request, IN_id):
    participante = Participantes.objects.get(id=IN_id)
    form = FormParticipantes(instance=participante)

    if request.method == 'POST':
        form = FormParticipantes(request.POST, instance=participante)
        if form.is_valid():
            form.save()
            return redirect('/participantes')

    data = {'form': form}
    return render(request, 'agregarParticipantes.html', data)

#API Rest Autor
class autorView(APIView):
    def get(self, request):
        autor = Autor.objects.all()
        serial = AutorSerial(autor, many=True)
        return Response(serial.data)
    
    def post(selt, request):
        serial = AutorSerial(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
#Class Based View Modelos Participantes
class participantes_list(APIView):
    def get(self, request):
        participante = Participantes.objects.all()
        serial = ParticipanteSerial(participante, many=True)
        return Response(serial.data)
    
    def post(selt, request):
        serial = ParticipanteSerial(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class participantes_id(APIView):
    def get_object(self, id):
        try:
            participante = Participantes.objects.get(pk=id)
        except Participantes.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, id):
        participantes = self.get_object(id)
        serial = ParticipanteSerial(participantes)
        return Response(serial.data)
    
    def put(self, request, id):
        participantes = self.get_object(id)
        serial = ParticipanteSerial(participantes, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        participantes = self.get_object(id)
        participantes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#Function Based View Modelos Instituciones
@api_view(['GET', 'POST'])
def instituciones_list(request):
    if request.method == 'GET':
        insti = Institucion.objects.all()
        serial = InstitucionSerial(insti, many=True)
        return Response(serial.data)

    if request.method == 'POST':
        serial = InstitucionSerial(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def instituciones_id(request, id):
    try:
        insti = Institucion.objects.get(id=id)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = InstitucionSerial(insti)
        return Response(serial.data)
    
    if request.method == 'PUT':
        serial = InstitucionSerial(insti, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        insti.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


