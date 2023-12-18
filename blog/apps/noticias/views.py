from django.shortcuts import render
from .models import Noticia, Categoria

# Create your views here.
def ListarNoticias(request):
    contexto = {}
    id_categoria = request.GET.get("id", None)

    if id_categoria:
        n = Noticia.objects.filter(categoria_noticia=id_categoria)
    else:
        n = Noticia.objects.all()

    #filtrar por antiguedad asc 
    antiguedad_asc = request.GET.get("antiguedad_asc")
    if antiguedad_asc:
        n = Noticia.objects.all().order_by('fecha_publicacion')
    
    #filtrar por antiguedad des 
    antiguedad_desc = request.GET.get("antiguedad_desc")
    if antiguedad_desc:
        n = Noticia.objects.all().order_by('-fecha_publicacion')

    #filtrar por orden alfabetico asc
    orden_asc = request.GET.get("orden_asc")
    if orden_asc:
        n = Noticia.objects.all().order_by('titulo')
    
    #filtrar por orden alfabetico desc
    orden_desc = request.GET.get("orden_desc")
    if orden_desc:
        n = Noticia.objects.all().order_by('-titulo')


    cat = Categoria.objects.all().order_by('nombre')
    contexto['noticias'] = n
    contexto['categorias'] = cat 
    
    return render (request, 'noticias/listar.html', contexto)

def DetalleNoticia(request, pk):
    contexto = {}

    n = Noticia.objects.get(pk = pk)
    contexto['noticias'] = n
    
    return render (request, 'noticias/detalle.html', contexto)

