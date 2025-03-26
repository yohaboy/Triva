from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView ,ListView
from .models import QuizModel,QuestionModel,ChoiceModel

def home(request):
    quizList = QuizModel.objects.all()
    context = {'quizList':quizList}
    
    return render(request , "base/index.html" , context = context)

def quizPage(request):
    
    quiz = QuizModel.objects.get()
    questionList = quiz.questions.all()
    choices = questionList.choices.all()

    context = {
        'questionList':questionList,
        'choices':choices
         }
    
    return render(request ,'base/quiz.html', context=context)

def rank(request):
    return render(request , "base/rank.html")

def profile(request):
    return render(request , 'base/profile.html')

    