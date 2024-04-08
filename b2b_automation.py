from extras.scripts import *
from django.utils.text import slugify

from dcim.choices import DeviceStatusChoices, SiteStatusChoices
from dcim.models import Device, DeviceRole, DeviceType, Site

class NewBranchScript(Script):

    class Meta:
        name = "New B2B Order"
        description = "Provision a new business connection"
        fieldsets = (
            ('First group', ('site_name', 'site_name2')),
            ('Second group', ('location_name', 'location_name2')),
        )
    
    site_name = StringVar(
        description="Name of the new site"
    )
    location_name = StringVar(
        description="Name of the new location"
    )
    site_name1 = StringVar(
        description="Name of the new site"
    )
    location_name1 = StringVar(
        description="Name of the new location"
    )