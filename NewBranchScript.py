from extras.scripts import *
from django.utils.text import slugify

from dcim.choices import DeviceStatusChoices, SiteStatusChoices
from dcim.models import Device, DeviceRole, DeviceType, Site


class NewBranchScript(Script):

    class Meta:
        name = "ONT Diagnostics"
        description = "Request a diagnostics health check for a given ONT"

    device = ObjectVar(
        description="Connection Reference of ONT to check",
        model=Device
    )

    def run(self, data, commit):

        return f"Journal entry created: {data}"
