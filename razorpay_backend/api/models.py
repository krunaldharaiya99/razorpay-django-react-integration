from django.db import models
from django.utils.translation import gettext_lazy as _
from api.enums import PaymentStatus

# Create your models here.

class Order(models.Model):
    name = models.CharField(_("Patient Name"), max_length=254, blank=False, null=False)
    amount = models.FloatField(_("Amount"), null=False, blank=False)
    status = models.IntegerField(_("Payment Status"), default=PaymentStatus.PENDING, blank=False, null=False)
    razorpay_order_id = models.CharField(_("Order ID"), max_length=40, null=False, blank=False)
    # razorpay_payment_id = models.CharField(_("Payment ID"), max_length=36, null=False, blank=False)
    # razorpay_signature = models.CharField(_("Signature ID"), max_length=128, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

