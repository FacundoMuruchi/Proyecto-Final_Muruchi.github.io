from django.shortcuts import render

def inicio(request):
    return render(
        request=request,
        template_name='home.html'
    )