from django.contrib import admin
from .models import Choice, Question, Form

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'choice', 'created_at', 'updated_at')
    search_fields = ('choice',)
    list_filter = ('created_at',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'question_type', 'created_at', 'updated_at')
    search_fields = ('question', 'question_type')
    list_filter = ('question_type', 'created_at')

@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'code', 'creator', 'created_at', 'updated_at')
    search_fields = ('title', 'code', 'creator__username')
    list_filter = ('created_at', 'creator')
    filter_horizontal = ('question',)  # For ManyToMany fields
