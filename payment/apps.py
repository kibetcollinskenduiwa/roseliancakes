from django.utils.translation import gettext_lazy as _

from oscar.core.application import OscarConfig


class PaymentConfig(OscarConfig):
    label = 'payment'
    name = 'payment'
    verbose_name = _('Payment')
