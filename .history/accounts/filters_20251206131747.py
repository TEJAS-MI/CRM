from dataclasses import field
import django_filters
from.models import *

class orderFilter(django_filters.filterset):
    class Meta:
        model=order
        fields=
