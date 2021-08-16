from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# from .models import Question #importacion de los modelos(bd) 
# from django.http import Http404


def home(request):
    return HttpResponse(render(request,'app_web/home.html'))

def detalle(request):
    return HttpResponse("detalle")

def about(request):
    return HttpResponse("about")



# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'app_web/detail.html', {'question': question})