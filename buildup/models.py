from django.db import models
from datetime import datetime

class Fact(models.Model):
    text = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_date = models.DateTimeField('date created')

fact = Fact(text='Giraffes sleep standing up', author='Steve Irwin', created_date=datetime.now())
fact = Fact(text='Monkeys are the best :D', author='Me(:', created_date=datetime.now())
fact = Fact(text='Kawaii ', author='Me(:', created_date=datetime.now())
fact.save()
facts = Fact.objects.all()
for fact in facts:
    print fact.id, fact.text, fact.created_date