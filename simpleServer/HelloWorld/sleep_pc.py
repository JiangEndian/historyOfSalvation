from django.http import HttpResponseRedirect 
from django.shortcuts import render
from MyPython3 import *
import os

def sleep(request):
    runsyscmd('/home/ed/bin/autosleep.bash 9999 9999')


    return HttpResponseRedirect('/alt1234')
