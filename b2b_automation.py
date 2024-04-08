from extras.scripts import *
from django.utils.text import slugify

from dcim.choices import DeviceStatusChoices, SiteStatusChoices
from dcim.models import Device, DeviceRole, DeviceType, Site
from tenancy.models import Tenant

class NewBranchScript(Script):

    class Meta:
        name = "New B2B Order"
        description = "Provision a new business connection"
        fieldsets = (
            ('Customer information', ('wholesale_provider', 'site_temp')),
            ('Site information', ('site_name', 'site_address')),
            ('Service Information', ('service_profile', 'site_temp1'))
        )
    
    wholesale_provider = ObjectVar(
        description = "The name of the reseller ordering this service",
        model = Tenant,
        query_params = {
            'group': 'wholesale-providers'
        }
    )
    site_name = StringVar(
        description = "Name of the site or business"
    )
    site_address = TextVar(
        description = "Name of the old location"
    )
    site_temp = StringVar()
    service_profile = ChoiceVar(
        choices = (
            ('1g_eth', '1G Ethernet Layer 2'),
            ('10g_eth', '10G Ethernet Layer 2'),
            ('1g_fttp', '1G FTTP')
        )
        description = "Type of service being provided"
    )
    site_temp1 = StringVar()
