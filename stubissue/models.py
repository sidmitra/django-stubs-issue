from __future__ import annotations

import uuid
from django.db import models
from django.conf import settings
from enum import Enum


class RequestState(Enum):
    CREATED = "created"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    ARCHIVED = "archived"
    FLAGGED = "flagged"

    CHOICES = (
        (CREATED, "Created"),
        (ACCEPTED, "Accepted"),
        (REJECTED, "Rejected"),
        (ARCHIVED, "Archived"),
    )


class SomeApprover(models.Model):
    approver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="request_approver",
    )
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        help_text="The person who added this approver. Null if user was in approval policy",
    )
    status = models.CharField(
        choices=RequestState.CHOICES.value,
        max_length=10,
        default=RequestState.CREATED.value,
        db_index=True,
    )
    is_active = models.BooleanField(
        default=True, help_text="False if an admin has removed this approver"
    )
    mute_comments = models.BooleanField(
        default=False,
        help_text="True if an approver has chosen to not receive new comments via email",
    )
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    last_notified_time = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)
