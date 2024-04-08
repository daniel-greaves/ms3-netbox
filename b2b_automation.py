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
            ('Customer Information', ('wholesale_provider')),
            ('Site Information', ('site_name', 'site_address')),
            #('Service Information', ('service_profile'))
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
