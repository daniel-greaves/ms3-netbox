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
        comments = data['comments']
        kind = data['kind']

        if commit:
            journal_entry = JournalEntry.objects.create(
                assigned_object=device,
                assigned_object_type=device.get_content_type(),
                created=now(),
                kind=kind,
                comments=comments
            )
            self.log_success(f"Journal entry successfully created for {device}")
        else:
            self.log_info(f"(Dry-run) Journal entry would be created for {device}")

        return f"Journal entry created: {comments}"
