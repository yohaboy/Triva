from django.contrib import admin
from .models import QuizModel,QuestionModel,ChoiceModel

admin.site.register(QuizModel)
admin.site.register(QuestionModel)
admin.site.register(ChoiceModel)
