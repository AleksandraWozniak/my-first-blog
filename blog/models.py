#!/usr/bin/python2
# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
# Create your models here.
# models.Model oznacza, że nasz obiekt Post jest modelem Django. 
# W ten sposób Django wie, że powinien go przechowywać w bazie danych
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
	# metoda publikująca wpis
    def publish(self):
        self.published_date = timezone.now()
        self.save()
		
	# metoda, w wyniku ktorej otrzymamy tekst (string) zawierający tytuł wpisu
    def __str__(self):
        return self.title