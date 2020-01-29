from django.db import models

# Create your models here.
#jak maja wygladac nasze dane

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DataTimeField(verbose_name="date published")

    def __str__(self):
        return f"{self.id} | {self.question_text}"

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE())
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.id} | {self.question.question_name} | {self.choice_text}"