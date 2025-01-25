from extras.scripts import *
from django.utils.text import slugify

from dcim.choices import DeviceStatusChoices, SiteStatusChoices
from dcim.models import Device, DeviceRole, DeviceType, Site
from netbox_inventory.models import Asset
from extras.models import JournalEntry

class NewBranchScript(Script):

    class Meta:
        name = "ONT Replacement"
        description = "Replace an ONT  for a given FTTP Connection"

    device = ObjectVar(
        description="Connection Reference of ONT to check",
        model=Device
    )

    new_ont = ObjectVar(
        label = "New ONT"
        description = "Serial Number of new ONT",
        model=Asset
    )

    def run(self, data, commit):
        device = data['device']



        return f"Journal entry created:"
