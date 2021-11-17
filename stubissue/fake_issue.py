from __future__ import annotations

from django.db.models import QuerySet, Count
from .models import SomeApprover


def my_fake_method() -> QuerySet[SomeApprover]:
    return (
        SomeApprover.objects
        .filter(is_active=True)
        .annotate(count=Count("status"))
    )
