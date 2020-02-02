from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# /hello
from polls.models import Question


def funkcja_widoku(request):
    html = """<!doctype html>
    <html>
    <head></head>
    <body>
    Hello Alx!!
    </body>
    </html>"""

    return HttpResponse(html)

# /hello/Rafał
def hello_name(request, name):
    html = f"""<!doctype html>
    <html>
    <head></head>
    <body>
    Hello {name}!!
    </body>
    </html>"""
    return HttpResponse(html)


# np: /sum/1/2
# /sum/<int:a>/<int:b>
# /mul/1/2

# /<op>/<int:a>/<int:b>
def operacje(request, op, a, b):
    if op == "sum":
        wynik = a + b


    return HttpResponse(wynik)


def index(request):
    return HttpResponse("Hello world! That's polls index")

def questions_list(request):
    qs = Question.objects.all()
    text = ""
    for q in qs:
        text += str(q)
        text += "<br>"

    return HttpResponse(text)

# zad domowe
# widok szczegółow

# questions/1

# questions/2
def question_details(): pass
# itd

# https://docs.djangoproject.com/en/3.0/intro/tutorial01/
# https://docs.djangoproject.com/en/3.0/intro/tutorial02/
# https://docs.djangoproject.com/en/3.0/intro/tutorial03/

#  Na środę - na egzamin:D -
# https://pythonprinciples.com/challenges/