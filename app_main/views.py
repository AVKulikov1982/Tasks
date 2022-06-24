from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import logging

logger = logging.getLogger(__name__)


def main(request):
	return render(request, 'index.html')

