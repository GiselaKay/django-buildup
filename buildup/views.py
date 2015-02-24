from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from buildup.models import Fact
import random
import subprocess
def hello(request):
    return HttpResponse("Hello world!")

def time(request):
    return HttpResponse("The time is " + str(datetime.now()))
def rand(request):
	return HttpResponse("Random Number: " + str(random.randint(1,100)))
def helloname(request, yourname):
	return HttpResponse("Hello " + yourname)
def speaks(request, speak):
	subprocess.call(["say", speak])
	return HttpResponse("Done")
def hello_template(request, yourname):
	return render(request, "hello.html", { "yourname": yourname, "foobar": "!!" })
def rand_template(request):
	return render(request, "random.html", {"rand": str(random.randint(1,100))})
def all_facts(request):
	return render(request, "all_facts.html", {"facts": Fact.objects.all()})