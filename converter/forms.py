from django.forms import ModelForm, CharField
from .models import Editor
from ckeditor.fields import CKEditorWidget


class EditorForms(ModelForm):
    body = CharField(
        widget=CKEditorWidget,
        label='Enter Your Text'
    )

    class Meta:
        model = Editor
        fields = '__all__'
