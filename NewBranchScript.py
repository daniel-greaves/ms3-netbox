from extras.scripts import *
from django.utils.text import slugify

from dcim.choices import DeviceStatusChoices, SiteStatusChoices
from dcim.models import Device, DeviceRole, DeviceType, Site
from netbox_inventory.models import Asset

class NewBranchScript(Script):

    class Meta:
        name = "New Branch"
        description = "Provision a new branch site"

    device = ObjectVar(
        description="Connection Reference of ONT to check",
        model=Device
    )

    new_ont = ObjectVar(
        description = "Serial Number of new ONT",
        model=Asset
    )

    def run(self, data, commit):
        device = data['device']

        journal_entry = JournalEntry.objects.create(
            assigned_object=device,
            assigned_object_type='dcim.device',
            created=now(),
            kind='info',
            comments='Pending...'
        )

        return f"Journal entry created:"
