from rest_framework import serializers
from .models import Choice, Question, Form

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'choice']

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'question', 'question_type', 'choices']

    def create(self, validated_data):
        # Handle creating the Question with choices
        choices_data = validated_data.pop('choices')
        question = Question.objects.create(**validated_data)
        for choice_data in choices_data:
            Choice.objects.create(question=question, **choice_data)
        return question

    def update(self, instance, validated_data):
        # Handle updating the Question and choices
        choices_data = validated_data.pop('choices', None)
        instance.question = validated_data.get('question', instance.question)
        instance.question_type = validated_data.get('question_type', instance.question_type)
        instance.save()

        if choices_data is not None:
            # Handle adding/removing choices
            instance.choices.clear()
            for choice_data in choices_data:
                Choice.objects.create(question=instance, **choice_data)

        return instance

class FormSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True)  # Allow nested writes for questions

    class Meta:
        model = Form
        fields = ['id', 'code', 'title', 'creator', 'question']

    def create(self, validated_data):
        questions_data = validated_data.pop('question')
        form = Form.objects.create(**validated_data)
        for question_data in questions_data:
            # Save each question along with its choices
            Question.objects.create(form=form, **question_data)
        return form

    def update(self, instance, validated_data):
        questions_data = validated_data.pop('question', None)
        instance.code = validated_data.get('code', instance.code)
        instance.title = validated_data.get('title', instance.title)
        instance.save()

        if questions_data is not None:
            instance.question.clear()
            for question_data in questions_data:
                # Update questions and their choices
                question = Question.objects.create(form=instance, **question_data)
                instance.question.add(question)

        return instance
