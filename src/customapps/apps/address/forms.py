# coding=utf-8
from oscar.apps.address.forms import AbstractAddressForm
from customapps.apps.address.models import UserAddress
from oscar.views.generic import PhoneNumberMixin


class UserAddressForm(PhoneNumberMixin, AbstractAddressForm):
    def __init__(self, user, *args, **kwargs):
        super(UserAddressForm, self).__init__(*args, **kwargs)
        self.instance.user = user

    class Meta:
        model = UserAddress
        fields = [
            'title', 'first_name', 'last_name',
            'line1', 'line2', 'line3', 'line4',
            'state', 'postcode', 'country',
            'phone_number', 'company_name','notes',
        ]
        
from oscar.apps.address.forms import *