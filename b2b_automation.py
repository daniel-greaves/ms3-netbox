from extras.scripts import *
from django.utils.text import slugify

from dcim.choices import DeviceStatusChoices, SiteStatusChoices
from dcim.models import Device, DeviceRole, DeviceType, Manufacturer, Site
from tenancy.models import Tenant

class NewBusinessService(Script):

    class Meta:
        name = "New B2B Order"
        description = "Provision a new business connection"
        fieldsets = (
            ('Order Information', ('wholesale_provider', 'order_reference')),
            ('Connection Information', ('site_name', 'site_address', 'connection_reference', 'olt_area')),
            ('Service Information', ('service_reference', 'service_profile'))
        )

    order_reference = StringVar(
        description = "Reference number of the order",
        regex = "^ORD\d{7}$"
    )

    connection_reference = StringVar(
        description = "Reference number of the service",
        regex = "^FTTP\d{6}$"
    )
    
    service_reference = StringVar(
        description = "Reference number of the service",
        regex = "^SERA\d{6}$"
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

    olt_area = ObjectVar(
        model = Device,
        description = "The OLT which the connection will be fed from",
        query_params = {
            'device_role': 'olt'
        }
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

        nte_role = DeviceRole.objects.get(slug='nte')
        
        if device_model:
            device_type = DeviceType.objects.get(model = device_model)
            nte = Device(
                device_type = device_type,
                name = f'{site.slug.upper()}-NTE-1',
                site = site,
                status = DeviceStatusChoices.STATUS_PLANNED,
                device_role = nte_role
            )
            nte.full_clean()
            nte.save()
            self.log_success(f"Created new NTE: {nte}")
