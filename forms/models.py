from django.db import models

# Create your models here.
CHOICES = (
    ('pa', 'Paragraph'),
    ('rd', 'Radio'),
    ('cb', 'CheckBox'),
    ('tx', 'text'),
    ('ta', 'textarea'),
)


class ElementRender:
    def __init__(self, etype):
        self.etype = etype

    def render(self, output):
        if self.etype == 'pa':
            return "<p>" + output + "</p>"


class Element(models.Model):
    e_type = models.CharField(max_length=2, choices=CHOICES, default='ta')
    value = models.CharField(max_length=1000, default="element filler")

    def display(self):
        er = ElementRender(self.e_type)
        return er.render(self.value)

    def __str__(self):
        return self.value


class Form(models.Model):
    name = models.CharField(max_length=250)
    fields = models.ManyToManyField(Element)

    def __str__(self):
        return self.name
