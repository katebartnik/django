from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

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
    questionList = Question.objects.all()
    return render(
        request,
        "question/list.html",
        {"questions": questionList}
    )

def question_details(request, id):
    question = Question.objects.get(pk=id)

    return render(
        request,
        "question/details.html",
        {"question": question}
    )


