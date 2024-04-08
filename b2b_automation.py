from extras.scripts import *
from django.utils.text import slugify

from dcim.choices import DeviceStatusChoices, SiteStatusChoices
from dcim.models import Device, DeviceRole, DeviceType, Site
from tenancy.models import Tenant

class NewBranchScript(Script):

    class Meta:
        name = "New B2B Order"
        description = "Provision a new business connection"
        #fieldsets = (
            #('Customer Information', ('wholesale_provider')),
            #('Site Information', ('site_name', 'site_address')),
            #('Service Information', ('service_profile'))
        #)
    

    site_name = StringVar(
        description = "Name of the site or business"
    )
    site_address = TextVar(
        description = "Name of the old location"
    )
    service_profile = ChoiceVar(
        choices = (
            ('1g_eth', '1G Ethernet Layer 2'),
            ('10g_eth', '10G Ethernet Layer 2'),
            ('1g_fttp', '1G FTTP')
        )
        description = "Type of service being provided"
    )
