from django.shortcuts import render
from .models import Topic

def index(request):
    """"Página principal do Learning_Log"""
    return render(request,'learning_logs/index.html')

def topics(request):
    """Mostrar todos os assuntos"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request,'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Mostrar um único assunto e todas as suas entradas."""
    topic = Topic.objects.get(id = topic_id)