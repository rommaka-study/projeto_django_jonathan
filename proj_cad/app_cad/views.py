from django.shortcuts import render
from .models import Usuario

# Create your views here.
def home(request):
    return render(request, 'usuarios/home.html')


def usuarios(request):
    if request.method == 'POST':
        # 1. Pegue os dados que vieram do formulário HTML
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        
        # 2. SALVE A INSTÂNCIA (letra minúscula), não a classe!
        novo_usuario.save() 
        
    # 3. Retorne a página ou a lista de usuários
     #django como python trabalha com dicionario

    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    
    return render(request, 'usuarios/usuarios.html',usuarios)

