# coding=utf-8
from oscar.apps.address.forms import AbstractAddressForm
from customapps.apps.partner.models import PartnerAddress
from oscar.views.generic import PhoneNumberMixin


class PartnerAddressForm(PhoneNumberMixin, AbstractAddressForm):
    def __init__(self, user, *args, **kwargs):
        super(PartnerAddressForm, self).__init__(*args, **kwargs)
        self.instance.user = user
        
    class Meta:
        model = PartnerAddress
        fields = ['company_name', 'name', 'line1', 'line2', 'line3', 'line4','state', 'postcode',]