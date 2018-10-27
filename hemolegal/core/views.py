from django.shortcuts import render, redirect
from django.views import View
from .models import Doador, Doacao, Endereco
from .forms import FormDoador, FormEndereco

class Home(View):
	"""EXIBIR TOP 5 DOADORES E CAMPANHAS QUE ESTEJAM EM ANDAMENTO. ALGO COMO NOTÍCIAS OU NOTAS SERIA INTERESSANTE EXIBIR TAMBÉM."""
	
	
	def get(self, request):
		doadores = Doador.objects.all()
		quant = len(doadores)
		return render(request, "core/home.html", {'quant':quant})


class CadastroDoador(View):

	def get(self, request):
		form = FormDoador()
		endereco = FormEndereco()
		return render(request, "core/cadastro_doador.html", {'form':form, 'endereco': endereco})

	def post(self, request):		
		
		endereco = Endereco.objects.create(		
				logradouro = request.POST['logradouro'],
				numero = request.POST['numero'],
				cidade = request.POST['cidade'],
				bairro = request.POST['bairro'],
				estado = request.POST['estado']
			)

		doador = Doador(nome = request.POST['nome'],
			   dt_nascimento = request.POST['nascimento'],
			   cpf = request.POST['cpf'],
			   telefone = request.POST['telefone'],
			   sexo = request.POST['sexo'],
			   sangue = request.POST['tipo_sangue']
			)

		doador.endereco = endereco
		doador.save()	

		return redirect('core:doadores')

class ListarDoadores(View):
	def get(self, request):
		doadores = Doador.objects.all()
		quant = len(doadores)

		return render(request, "core/doadores.html", {'doadores':doadores, 'quant':quant})


class DetalheDoador(View):
	def get(self, request, *args, **kwargs):
		doador_id = self.kwargs['doador_id']
		doador = Doador.objects.get(pk = doador_id)

		return render(request, "core/detalhe_doador.html", {'doador': doador})

class DetalheDoacao(View):
	def get(self, request, *args, **kwargs):
		doacao_id = self.kwargs['doacao_id']
		doacao = Doacao.objects.get(pk = doacao_id)

		return render(request, "core/detalhe_doacao.html", {'doacao': doacao})