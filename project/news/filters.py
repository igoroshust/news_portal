import django_filters
from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput # ???
from .models import Article

# class NewsFilter(django_filters.FilterSet):
#     class Meta:
#         """Указываем Django-модель, в которой фильтруются записи"""
#         model = Article
#         fields = {
#             'name': ['icontains'],
#             'category': ['exact'],
#             'date': [
#                 'day__gt',
#             ],
#         }

class NewsFilter(django_filters.FilterSet):
    added_after = DateTimeFilter(
        field_name="date",
        lookup_expr="gt",
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'}
        ),
    )

    class Meta:
        model = Article
        fields = {
            'name': ['icontains'],
            'category': ['exact'],
        }

