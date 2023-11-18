from django.shortcuts import render, redirect
from .models import Usuario, Post
from .forms import UserForm, PostForm
from django.urls import reverse

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

# CREAR CUENTA

def crear_cuenta(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user=Usuario(name=data["name"], surname=data["surname"], password=data["password"], age=data["age"], email=data["email"])
            user.save()

            url_exitosa = reverse("exito")
            return redirect(url_exitosa)
    else:
        form = UserForm()

    return render(
        request=request,
        template_name="blog/cuenta.html",
        context={"form":form}
    )
        
# CUENTA CREADA
    
def exito(request):
    return render(request, "blog/exito.html")

# VER CUENTAS

def usuarios(request):
    return render(
        request=request,
        template_name="blog/usuarios.html",
        context={"usuarios": Usuario.objects.all()}
    )

# VER POSTS

def posts(request):
    return render(request,
                  "blog/posts.html",
                  context={"post": Post.objects.all()})

# BUSCAR POST

def buscar_post(request):
    if request.method == "POST":
        data = request.POST
        post = Post.objects.filter(name__contains=data["search"].title())

        return render(
            request=request,
            template_name="blog/posts.html",
            context={"post":post}
        )

# SUBIR POSTS

def subir(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            post = Post(name=data["name"].title(), author=data["author"].title(), text=data["text"], post=data["post"])
            post.save()

            return redirect("posts")
        
    else:
        form = PostForm

    return render(request,"blog/subir.html", context={"form": form})
    if request.method == "POST":
        form = PoemForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            story = Poema(name=data["name"].title(), text=data["text"], author=data["author"].title())
            story.save()

            url_exitosa = reverse("posts")
            return redirect(url_exitosa)
    else:
        form = PoemForm()

    return render(
        request=request,
        template_name="blog/subir_poema.html",
        context={"poem": form}
    )

# ELIMINAR POSTS

def eliminar_post(request,id):
    cuento = Post.objects.get(id=id)
    if request.method == "POST":
        cuento.delete()
        return redirect('posts')
    
# EDITAR

def editar_curso(request, id):
   curso = Curso.objects.get(id=id)
   if request.method == "POST":
       formulario = CursoFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           curso.nombre = data['nombre']
           curso.comision = data['comision']
           curso.save()
           url_exitosa = reverse('listar_cursos')
           return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'nombre': curso.nombre,
           'comision': curso.comision,
       }
       formulario = CursoFormulario(initial=inicial)
   return render(
       request=request,
       template_name='estudiantes/formulario_curso.html',
       context={'formulario': formulario},
   )
