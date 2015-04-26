from django.shortcuts import render
from django.http import HttpResponse

from .models import Business

def index(request):
	business_list = Business.objects.all()
	output = ', '.join([p.name for p in business_list])
	return HttpResponse(output)

    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = RequestContext(request, {
    #     'latest_question_list': latest_question_list,
    # })
    #return HttpResponse(template.render(context))


    #return HttpResponse("This is the Index page for our DataScience Capstone Project")