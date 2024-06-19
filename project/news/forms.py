from django import forms
from django.core.exceptions import ValidationError
from .models import Article, Category
from django.utils.translation import gettext_lazy as _

class NewsForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'name',
            'text',
            'category',
        ]
        labels = {
            'name': _('Name'),
            'text': _('Text'),
            'category': _('Category'),
        }


        def clean(self):
            cleaned_data = super().clean()
            name = cleaned_data.get("name")
            category = cleaned_data.get("category")
            date = cleaned_data.get("date")

            if name == category:
                raise ValidationError(
                    "Описание не должно совпадать и именем категории"
                )

            return cleaned_data