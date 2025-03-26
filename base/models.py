from django.db import models

class QuizModel(models.Model):
    subjects = [

        ('English','English'),
        ('Maths','Maths'),
        ('Biology','Biology'),
        ('Chemistry','Chemistry'),
    ]
    streams = [
        ('natural','natural'),
        ('social','social')
    ]
    stream = models.CharField(max_length=255 ,choices=streams ,default='natural')
    category = models.CharField(max_length= 255 ,choices=subjects)
    questionSize = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category
    
class QuestionModel(models.Model):
    quiz = models.ForeignKey(QuizModel ,on_delete=models.CASCADE ,related_name='questions')
    question = models.TextField()

    def __str__(self):
        return self.question

class ChoiceModel(models.Model):
    question = models.ForeignKey(QuestionModel,on_delete=models.CASCADE,related_name='choices')
    choice = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice

