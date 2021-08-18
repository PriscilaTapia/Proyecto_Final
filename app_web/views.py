from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Noticias #importacion de los modelos(bd) 



def home(request):
    all_noticias = Noticias.objects.all()
    
    context = { 'all_noticias':all_noticias}
    return render(request,'app_web/home.html',context)
    

def detalle(request):
    return HttpResponse(render(request,'app_web/detalle.html'))

def about(request):
    return HttpResponse(render(request,'app_web/about.html'))



# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'app_web/detail.html', {'question': question})