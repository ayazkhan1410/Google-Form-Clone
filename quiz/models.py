from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    class Meta:
        abstract = True
    
class Choice(BaseModel):
    choice = models.CharField(max_length=200)
    
    def __str__(self):
        return self.choice
    
    class Meta:
        ordering = ['id']


QUESTION_CHOICE = (
    ('Short answer', "Short answer"),
    ('Long answer', 'Long answer'),
    ('Multiple choice', 'Multiple choice'),
    ('Checkbox', 'Checkbox')
)
class Question(BaseModel):
    question = models.CharField(max_length=255, null=True, blank=True)
    question_type = models.CharField(max_length=255, choices=QUESTION_CHOICE)
    choices = models.ManyToManyField(Choice, related_name='question_choices', blank=True)

    def __str__(self):
        return f"{self.question} - {self.question_type}"

    class Meta:
        ordering = ["id"]

class Form(BaseModel):
    code = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='form_user')
    question = models.ManyToManyField(Question, related_name='forms')

    def __str__(self):
        return f"{self.title} - {self.creator}"
    
    class Meta:
        ordering = ["id"]
