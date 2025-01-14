from extras.scripts import *
from django.utils.text import slugify
from circuits.models import Provider, Circuit, ProviderNetwork, VirtualCircuit, VirtualCircuitTermination
from dcim.models import Device, Interface
from netbox_inventory.models import Asset

import json

class RunCommand(Script):

    class Meta:
        name = "Get ONT Asset"
        description = "Get ONT Asset"

        ont = ObjectVar(
            model=Asset,
            label="ONT",
            description="ONT",
            required=True
        )

def run(self, data, commit):

    self.log_info(f"ONT: {data['ont']}")
    return ("Done")
