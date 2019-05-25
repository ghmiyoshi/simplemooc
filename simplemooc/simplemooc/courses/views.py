from django.shortcuts import render, get_object_or_404

from .models import Course

def index(request):
    courses = Course.objects.all() # Retorna todos os cursos cadastrados no BD
    context = {'courses': courses}
    template_name = 'courses/index.html'

    return render(request, template_name, context)

# def details(request, pk):
#     course = get_object_or_404(Course, pk=pk) # Retorna um curso onde o pk é o id, esse parâmetro vem da urls.py
#                                               # Caso não encontre o curso será apresentado uma página 404
#     context = {'course':course}
#     template_name = 'courses/details.html'
#
#     return render(request, template_name, context)

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)

    context = {'course':course}
    template_name = 'courses/details.html'

    return render(request, template_name, context)



