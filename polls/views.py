#funkcje widokow

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# /hello
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
    return HttpResponse("Hello World! That's polls index")
