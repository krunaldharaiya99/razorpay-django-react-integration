from django.db import models
from django.utils.translation import gettext_lazy as _


class PaymentStatus(models.IntegerChoices):
    FAIL = 0, _("Fail")
    SUCCESSFULL = 1, _("Successfull")
    PENDING = 2, _("Pending")