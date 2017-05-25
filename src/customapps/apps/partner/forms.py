# coding=utf-8
from oscar.apps.address.forms import AbstractAddressForm
from customapps.apps.address.models import UserAddress
from oscar.views.generic import PhoneNumberMixin


class PartnerAddressForm(PhoneNumberMixin, AbstractAddressForm):
    class Meta:
        model = PartnerAddress
        fields = [
            'customer_name', 'detail_address','line2','line3', 'line4', 'phone_number',
            'postcode','state','country'
        ]
        exclude = [
            'title', 'first_name', 'last_name',
            'search_text'
        ]
        labels = {
            "line3": u"Landmark",
            "postcode": u"Pincode",
            "state": u"State",
        }
