from django.shortcuts import render
from .forms import SubmitForm 
from home.models import Grupo, Participante, Boletim

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

# Create your views here.

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from django.http import HttpResponse
from PyPDF2 import PdfFileWriter, PdfFileReader

from django.http import FileResponse, Http404

def pdf_view(request, boletim_numero):
	boletim = Boletim.objects.get(numero=boletim_numero)
	url = boletim.arquivo.url
	url = url[1:]
	try:
		return FileResponse(open(url, 'rb'), content_type='application/pdf')
	except FileNotFoundError:
		raise Http404()


def index(request):
	boletins = Boletim.objects.all()

	args = {'boletins': boletins}

	return render(request, 'home/home.html', args)

def envolvidos(request):
	return render(request, 'home/envolvidos.html')

def checkin(request):
	return render(request, 'home/checkin.html')

def pre_checkin(request):
	return render(request, 'home/pre_checkin.html')

def submit(request):
	if request.method == "POST":
		print(request.FILES)
		#dados do participante
		nome_part = request.POST.get('nome_part').upper()
		idade_part = request.POST.get('idade_part')
		email_part = request.POST.get('email_part')

		#dados do grupo
		nome_grupo = request.POST.get('nome_grupo').upper()
		numeral_grupo = request.POST.get('numeral_grupo')
		estado_grupo = request.POST.get('estado_grupo').upper()
		nome_diretor = request.POST.get('nome_diretor').upper()
		email_diretor = request.POST.get('email_diretor')

		#arquivos
		ficha_medica = request.FILES['ficha_medica']
		autorizacao = request.FILES['autorizacao']
		print(ficha_medica)

		#salva o grupo no banco de dados
		try:
			grupo = Grupo.objects.get(nome=nome_grupo, numeral=numeral_grupo, estado=estado_grupo)
		except Grupo.DoesNotExist:
			grupo = None

		if grupo is None:
			grupo = Grupo(nome=nome_grupo, numeral=numeral_grupo, estado=estado_grupo, diretor=nome_diretor, email_diretor=email_diretor)	
			grupo.save()

		#salva o participante no banco de dados
		participante = Participante(nome=nome_part, idade=idade_part, email=email_part, grupo=grupo, ficha_medica=ficha_medica, autorizacao=autorizacao)
		participante.save()
	return render(request, 'home/agradecimento.html')
