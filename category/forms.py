
from django.forms import Form, CharField, Textarea


class ContactForm(Form):
    fullname = CharField(max_length=32)
    remarks = CharField(widget=Textarea)
