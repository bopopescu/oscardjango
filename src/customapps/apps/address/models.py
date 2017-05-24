# coding=utf-8
from django.utils.translation import ugettext_lazy as _
from oscar.apps.address.abstract_models import AbstractUserAddress
from django.db import models
from django.core import exceptions



class UserAddress(AbstractUserAddress):
	company_name = models.CharField(_("company name"), max_length=255, blank=True)
	pan_number = models.CharField(_("PAN number"), max_length=10, blank=True)












from oscar.apps.address.models import *  # noqa
