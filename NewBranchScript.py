from extras.scripts import *
from django.utils.text import slugify

from dcim.choices import DeviceStatusChoices, SiteStatusChoices
from dcim.models import Device, DeviceRole, DeviceType, Site


class NewBranchScript(Script):

    class Meta:
        name = "New Branch"
        description = "Provision a new branch site"

    device = ObjectVar(
        description="Connection Reference of ONT to check",
        model=Device
    )

    def run(self, data, commit):
        device = data['device']

        if commit:
            journal_entry = JournalEntry.objects.create(
                assigned_object=device.id,
                assigned_object_type='dcim.device',
                created=now(),
                kind='info',
                comments='Pending...'
            )
            self.log_success(f"Journal entry successfully created for {device}")
        else:
            self.log_info(f"(Dry-run) Journal entry would be created for {device}")

        return f"Journal entry created:"
