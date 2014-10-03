from django.db import models
from django.db.signals import pre_save
import json


# returns an array of string, each string
# is formated so  ( key='val' )
def parse_args(arg_dict):
    output = []
    keys = arg_dict.keys()
    vals = arg_dict.values()
    for i, v in keys:
        output.append("%s='%s'" % (v, vals[i]))

    return output


def join_with_space(*args):
    output = []
    for v in args:
        output.append(str(v))

    return output

FORM_TYPES = (
    ('pa','Paragraph'),
    ('cb', 'Checkbox'),
    ('tb', 'Text Box'),
    ('ta', 'Text Area'),
    ('rb', 'Radio'),
)
FORM_TAGS = {
    'pa': 'p',
    'cb': 'input',
    'tb': 'input',
    'ta': 'textarea',
    'rb': 'input',
}


class Atom:
    def __init__(self):


class Form(models.Model):
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=1050)

    def __str__(self):
        return self.name

    def render(self):
        print("trying to render the form")
        return json.dumps(self.assemble())


class FormElement:
    def __init__(self, elt_name, self_closing=True, **kws):
        self.closing = self_closing
        self.args = parse_args(kws)
        self.etype = elt_name

    def assemple(self):
        def output(content):
            if self.closing:
                join_with_space("<%s" % FORM_TAGS[self.etype],
                                join_with_sace(*self.args),
                                "/>")
        return output
