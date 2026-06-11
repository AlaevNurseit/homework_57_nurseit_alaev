from django import forms
from .models import Issue, Status, Type


class IssueForm(forms.ModelForm):
    summary = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}),required=True,label="Краткое описание",error_messages={"required": "Обязательное поле"})
    description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "rows": "5"}),required=False,label="Полное описание" )
    status = forms.ModelChoiceField(queryset=Status.objects.all(),widget=forms.Select(attrs={"class": "form-select"}),label="Статус")
    types = forms.ModelMultipleChoiceField(queryset=Type.objects.all(),widget=forms.CheckboxSelectMultiple,label="Типы")

    class Meta:
        model = Issue
        fields = ('summary', 'description', 'status', 'types')