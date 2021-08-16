from django.urls import path
from app_web import views

urlpatterns = [
    path("", views.home, name="home"),
    path("detalle/", views.detalle, name="detalle"),
    path("about/", views.about, name="about"),
]

#para agregar contenido de la base de datos usar el ID de cada noticia

# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),

#     # ex: /polls/5/deberia de ir a la noticia en especifico
#     path('noticia/<int:question_id>/', views.detail, name='detail'),

#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),

#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),

# ]