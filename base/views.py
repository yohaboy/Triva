from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView ,ListView
from .models import QuizModel,QuestionModel,ChoiceModel

def home(request):
    query = request.GET.get('query')
    if query:
        quizList = QuizModel.objects.filter(stream__icontains=query)
    else :
        quizList = QuizModel.objects.filter(stream__icontains = 'natural')

    context = {'quizList':quizList}
    
    return render(request , "base/index.html" , context = context)

def quizPage(request,id):
    
    quiz = get_object_or_404(QuizModel, id=id)
    questionList = QuestionModel.objects.filter(quiz=quiz).prefetch_related("choices")

    context = {
        'questionList':questionList,
         }
    
    return render(request ,'base/quiz.html', context=context)

def rank(request):
    return render(request , "base/rank.html")

def profile(request):
    return render(request , 'base/profile.html')

    