# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question

#def index(request):
#    return HttpResponse("Olá! Você está no índice da enquete.")
#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('polls/index.html')
#    context = {
#        'latest_question_list': latest_question_list,
#    }
#    return HttpResponse(template.render(context, request))
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

#def detail(request, question_id):
#    return HttpResponse("Voce esta acessando a enquete %s." % question_id)
#def detail(request, question_id):
#    try:
#        question = Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("Enquete não existe.")
#    return render(request, 'polls/detail.html', {'question': question})
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "Voce esta acessando o resultado da enquete %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Voce esta acessando a votacao da enquete %s." % question_id)