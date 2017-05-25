# coding=utf-8
from django.utils.translation import ugettext_lazy as _
from oscar.apps.address.abstract_models import AbstractUserAddress
from django.db import models
from django.core import exceptions


class UserAddress(AbstractUserAddress):
    customer_name = models.CharField(_("Name"), max_length=255, blank=True)
    detail_address = models.CharField(
        _("Shipping address:"), max_length=255, blank=True,
        help_text=u"It is advisable to fill in the detailed receipt address, such as street name, house number, floor and room number")

    def clean(self):
        # Strip all whitespace
        for field in ['customer_name', 'detail_address','line2','line3', 'line4', 'phone_number','postcode','state']:
            if self.__dict__[field]:
                self.__dict__[field] = self.__dict__[field].strip()

    def _update_search_text(self):
        search_fields = filter(
            bool, [self.line1, self.line4, self.line2, self.detail_address,
                   self.postcode, self.customer_name, self.country.name])
        self.search_text = ' '.join(search_fields)

    @property
    def salutation(self):
        return self.customer_name

    @property
    def name(self):
        return self.customer_name

    def active_address_fields(self, include_salutation=True):
        """
        Return the non-empty components of the address, but merging the
        title, first_name and last_name into a single line.
        """
        fields = [self.line1, self.line4, self.line2,
                  self.detail_address, self.postcode]
        if include_salutation:
            fields = [self.salutation] + fields
        fields = [f.strip() for f in fields if f]
        try:
            fields.append(self.country.printable_name)
        except exceptions.ObjectDoesNotExist:
            pass
        return fields


from oscar.apps.address.models import *