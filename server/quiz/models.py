from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=50)
    correct_answer = models.ManyToManyField("Question", related_name='quiz_correct_answer')
    variant = models.ForeignKey("Question", on_delete=models.CASCADE, related_name='quiz_variant')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Quiz'
        verbose_name_plural='Quizes'


class Question(models.Model):
    question = models.CharField(max_length=50)

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name='question'
        verbose_name_plural='questions'
