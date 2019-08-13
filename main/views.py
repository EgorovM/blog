# -*- coding: utf-8 -*-

from django.shortcuts 			import render, HttpResponseRedirect, redirect, HttpResponse
from .models					import Section, Post
from django.db 					import IntegrityError
from django.core.paginator 		import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth 		import authenticate, logout
from django.contrib 			import auth
from PIL      					import Image
from pytz 						import timezone
from datetime 					import datetime, timedelta
from io import StringIO
import sqlite3
import pytz

def index(request):

    return render(request, 'main/index.html');

def section(request):
    context = {}

    return render(request, 'main/section.html', context);

    # try:
    #     section = Section.objects.get(name = view_section_name)
    #
    #     context['view_section'] = section
    #
    #     return render(request, 'main/section.html', context);
    #
    # except Section.DoesNotExist:
    #     return render(request, 'main/404.html')


def post(request):
    context = {}

    return render(request, 'main/post.html', context);
