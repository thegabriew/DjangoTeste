from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World")

def nome(request):
    return HttpResponse("Meu nome é")

def kanye(request):
    return HttpResponse("ye is the goat")