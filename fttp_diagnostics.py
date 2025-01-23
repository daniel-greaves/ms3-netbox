from extras.scripts import Script
from dcim.models import Device
from extras.models import JournalEntry
from utilities.forms.fields import DynamicModelChoiceField
from django.utils.timezone import now

class AddDeviceJournalEntry(Script):
    class Meta:
        name = "Add Journal Entry to Device"
        description = "Select a device and add a journal entry."
        field_order = ['device', 'entry']

    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        label="Select Device",
        required=True
    )

    entry = Script.StringVar(
        description="Journal entry text",
        required=True
    )

    def run(self, data, commit):
        device = data['device']
        entry_text = data['entry']

        try:
            # Create the journal entry for the selected device
            journal_entry = JournalEntry.objects.create(
                assigned_object=device,
                assigned_object_type=device.get_content_type(),
                created=now(),
                kind=JournalEntry.KindChoices.INFO,  # Adjusting for NetBox v4's choice fields
                comments=entry_text
            )

            if commit:
                self.log_success(f"Journal entry successfully added to device: {device}")
            else:
                self.log_info(f"Dry run: Journal entry would have been added to device: {device}")

            return f"Journal entry added: {entry_text}"

        except Exception as e:
            self.log_failure(f"Error adding journal entry: {e}")
            return f"Failed to add journal entry: {e}"
