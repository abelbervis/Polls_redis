from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Question
from polls.tasks import *
#redis
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

def incrCounterView(nameView,initial_state=1,incr=True):
    my_counter = cache.get_or_set(nameView + '_counter', initial_state)
    if incr:
        cache.incr(nameView + '_counter')
    return my_counter

#@cache_page(CACHE_TTL)
def index(request):
    global incrCounterView
    my_counter = incrCounterView(request.resolver_match.view_name)
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
    #details_counter = cache.get_or_set('detail_counter', 0)
    details_counter = 0
    if len(latest_question_list) > 0:
        for element in latest_question_list:
            print(element.id)
            element.counter_views = incrCounterView('detail'+str(element.id),0,False)
            details_counter+= int(element.counter_views)

    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
        'my_counter':my_counter,
        'details_counter':details_counter,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    global incrCounterView
    my_counter = incrCounterView(request.resolver_match.view_name + str(question_id))
    my_counter = int(my_counter) + 1
    template = loader.get_template('polls/details.html')
    context = {
        'my_counter':my_counter,
        'question_id':question_id
    }
    return HttpResponse(template.render(context, request))

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)




def send_mail(request):
    if request.method=='GET':
        return render(request,'polls.html')
    else:
        sender=request.POST.get('sender','')
        sender_password=request.POST.get('sender_password','')
        receiver=request.POST.get('receiver','')
        message=request.POST.get('message','')

        for i in range(1,3):
            task_send_mail(sender,sender_password,receiver,message)

        return HttpResponse('vista mensajes..')