from rest_framework import viewsets, response

from quiz.models import Question
from quiz.serializer import QuizSerializer

class QuizViewSet(viewsets.ViewSet):
    
     def list(self, request):
        queryset = Question.objects.all()
        serializer = QuizSerializer(queryset, many=True)
        return response.Response(serializer.data)

