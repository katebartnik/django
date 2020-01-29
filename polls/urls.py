from django.urls import path

from polls.views import funkcja_widoku, hello_name, operacje, index

urlpatterns = [
    path("", index, name="index"),
    path('hello/', funkcja_widoku),
    path('hello/<name>', hello_name),
    path('<op>/<int:a>/<int:b>', operacje),

]
