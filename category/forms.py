
from django.forms import Form, CharField, Textarea, TextInput, ChoiceField


class ContactForm(Form):
    fullname = CharField(max_length=32, 
                         widget=TextInput(attrs={'class': 'form-control'}))
    remarks = CharField(widget=Textarea(attrs={'class': 'form-control'}), 
                        required=False)


class CategoryForm(Form):
    name = CharField(max_length=32)
    description = CharField(widget=Textarea(attrs={'class': 'form-control'}),
                            required=False)
    category = ChoiceField(required=False)
