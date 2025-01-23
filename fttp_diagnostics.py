from extras.scripts import Script
from dcim.models import Device
from utilities.forms.fields import DynamicModelChoiceField

class SelectDeviceScript(Script):
    class Meta:
        name = "Select a Device"
        description = "Prompts the user to select a device from the NetBox inventory."
        field_order = ['device']

    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        label="Select Device",
        required=True
    )

    def run(self, data, commit):
        selected_device = data['device']
        self.log_success(f"Selected device: {selected_device}")
        return f"Device selected: {selected_device}"
