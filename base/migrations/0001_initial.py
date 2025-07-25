# Generated by Django 5.1.3 on 2025-03-26 10:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='QuizModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream', models.CharField(choices=[('natural', 'natural'), ('social', 'social')], default='natural', max_length=255)),
                ('category', models.CharField(choices=[('English', 'English'), ('Maths', 'Maths'), ('Biology', 'Biology'), ('Chemistry', 'Chemistry')], max_length=255)),
                ('questionSize', models.PositiveIntegerField()),
                ('duration', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChoiceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=255)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='base.questionmodel')),
            ],
        ),
        migrations.AddField(
            model_name='questionmodel',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='base.quizmodel'),
        ),
    ]
