from django import forms
from django.forms import ModelForm
from .models import Project, Message


# Create a form to add new projects
class NewProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'image', 'project_url')

    #  function to add a bootsrap class to all fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            new_class = {
                "class": "form-control"
            }

        self.fields[str(field)].widget.attrs.update({
            **new_class
        })

        self.fields['description'].widget.attrs.update({
            'rows': '4'
        })


# Create a form to add new message from users
class NewMessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'email', 'message_body')

    #  function to add a bootsrap class to all fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            new_class = {
                "class": "form-control"
            }

        self.fields[str(field)].widget.attrs.update({
            **new_class
        })

        self.fields['message_body'].widget.attrs.update({
            'rows': '3'
        })
