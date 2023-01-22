from django.http import HttpResponse


def home(request):
    # takes request and returns the response
    return HttpResponse('<h1>Hello world</h1>')
