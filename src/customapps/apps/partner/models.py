# coding=utf-8
from django.utils.translation import ugettext_lazy as _
from oscar.apps.address.abstract_models import AbstractUserAddress
from django.db import models
from django.core import exceptions


class PartnerAddress(AbstractUserAddress):
    customer_name = models.CharField(_("Name"), max_length=255, blank=True)
    detail_address = models.CharField(
        _("Shipping address:"), max_length=255, blank=True,
        help_text=u"It is advisable to fill in the detailed receipt address, such as street name, house number, floor and room number")

    def clean(self):
        # Strip all whitespace
        for field in ['customer_name', 'detail_address','line2','line3', 'line4', 'phone_number','postcode','state']:
            if self.__dict__[field]:
                self.__dict__[field] = self.__dict__[field].strip()


from oscar.apps.partner.models import *
