from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=50)
    variant = models.ManyToManyField("Answer", related_name='quiz_correct_answer')
    correct = models.ForeignKey("Answer", on_delete=models.CASCADE, related_name='quiz_variants')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Quiz'
        verbose_name_plural='Quizes'


class Answer(models.Model):
    question = models.CharField(max_length=50)

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name='Answer'
        verbose_name_plural='Answers'
