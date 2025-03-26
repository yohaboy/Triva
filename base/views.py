from django.shortcuts import render
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

def quizPage(request , id):
    
    quiz = QuizModel.objects.get(id = id)
    questionList = quiz.questions.all()
    # choices = questionList.choices.all()

    context = {
        'questionList':questionList,
        # 'choices':choices
         }
    
    return render(request ,'base/quiz.html', context=context)

def rank(request):
    return render(request , "base/rank.html")

def profile(request):
    return render(request , 'base/profile.html')

    