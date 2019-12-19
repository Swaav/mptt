from django.shortcuts import render
from mpttassesment.models import MyFile


def show_myfile(request):
    return render(request, 'myfile.html',
                  {'myfile': MyFile.objects.all()})