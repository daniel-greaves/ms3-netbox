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
            ('Customer information', ('wholesale_provider', 'service_profile')),
            ('Site information', ('site_name', 'site_address')),
            #('Service Information', ('service_profile', 'site_temp1'))
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
    
    CHOICES = (
        ('1g_eth', '1G Ethernet Layer 2'),
        ('10g_eth', '10G Ethernet Layer 2'),
        ('1g_fttp', '1G FTTP'),
    )
    service_profile = ChoiceVar(
        choices=CHOICES
    )


    def run(self, data, commit):
        # Create the new site
        site = Site(
            name=data['site_name'],
            slug=slugify(data['site_name']),
            status=SiteStatusChoices.STATUS_PLANNED,
            physical_address = data['site_address']
        )
        site.full_clean()
        site.save()
        self.log_success(f"Created new site: {site}")

        # Create the NTE
        if data['service_profile'] == '1g_eth':
            device_model = 'FSP 150-GE104(E)'
        elif data['service_profile'] == '10g_eth':
            device_model = 'FSP 150-XG108'
        else:
            device_model = None

        nte_role = DeviceRole.objects.get(name='NTE')
        
        if device_model:
            device_type = DeviceType.objects.get(name = device_model)
            nte = Device(
                device_type = device_type
                name = f'{site.slug.upper()}-NTE-1',
                site = site,
                status = DeviceStatusChoices.STATUS_PLANNED,
                device_role = nte_role
            )
            nte.save()
            self.log_success(f"Created new NTE: {nte}")
