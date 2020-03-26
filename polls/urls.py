from django.urls import path
from polls.views import funkcja_widoku, hello_name, operacje, index, questions_list, question_details

urlpatterns = [
    path("", index, name="index"),
    path('hello/', funkcja_widoku),
    path('hello/<name>', hello_name),
    path('<op>/<int:a>/<int:b>', operacje),
    path("pytanie/", questions_list, name="question-list"),
    path("questions/<id>", question_details, name="question-details")
]