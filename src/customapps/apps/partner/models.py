# coding=utf-8
from django.utils.translation import ugettext_lazy as _
from oscar.apps.address.abstract_models import AbstractPartnerAddress
from django.db import models
from django.core import exceptions


class PartnerAddress(AbstractPartnerAddress):
    company_name = models.CharField(_("Company Name"), max_length=255, blank=True)
    
    def clean(self):
        # Strip all whitespace
        for field in ['company_name', 'name', 'line1', 'line2', 'line3', 'line4','state', 'postcode','country']:
            if self.__dict__[field]:
                self.__dict__[field] = self.__dict__[field].strip()
    


  
from oscar.apps.partner.models import *
