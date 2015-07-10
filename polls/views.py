from django.http import HttpResponse, Http404
# from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from .models import Question

# Create your views here.

def index(request):
    last_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ','.join([p.question_text for p in last_question_list])
    # template = loader.get_template('polls/index.html')
    # context = RequestContext(request,{
    #     'last_question_list':last_question_list
    # })
    context = {'last_question_list': last_question_list}
    # return HttpResponse(template.render(context))
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
