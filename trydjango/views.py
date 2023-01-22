from django.http import HttpResponse


def home_view(request):
    # takes request and returns the response
    return HttpResponse('<h1>Hello world</h1>')
