from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('Estudantes', EstudantesView.as_view(), name='estudantes'),
    path('cursos/', CursosView.as_view(), name='cursos'),
    path('pessoas/', PessoasView.as_view(), name='pessoas'),
    path('ocupacoes/', OcupacoesView.as_view(), name='ocupacoes'),
    path('instituicoes/', InstituicoesView.as_view(), name='instituicoes'),
    path('areasdosaber/', AreasdosaberView.as_view(), name='areasdosaber'),
    path('turnos/', TurnosView.as_view(), name='turnos'),
    path('Disciplinas/', DisciplinasView.as_view(), name='disciplinas'),
    path('matriculas/', MatriculasView.as_view(), name='matriculas'),
    path('avaliacoes/', AvaliacoesView.as_view(), name='avaliacoes'),
    path('frequencias/', FrequenciasView.as_view(), name='frequencias'),
    path('turmas/', TurmasView.as_view(), name='turmas'),
    path('cidade/', CidadesView.as_view(), name='cidades'),
    path('ocorrencias/', OcorrenciasView.as_view(), name='ocorrencias'),
    path('disciplinaporcurso/', DisciplinacursoView.as_view(), name='disciplinasporcurso'),
    path('tiposdeavaliacao/', TiposdeavaliacaoView.as_view(), name='tiposdeavaliacao')
]

