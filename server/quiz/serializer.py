from rest_framework import serializers

from quiz.models import Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):
    variant = AnswerSerializer(many=True)
    class Meta:
        model = Question
        fields = ('title', 'variant', 'correct')
