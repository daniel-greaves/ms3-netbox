from dcim.models import Site, Device, DeviceType
from django.utils.text import slugify
from extras.choices import JournalEntryKindChoices
from extras.scripts import *
from extras.models import JournalEntry
from netbox_inventory.models import Asset
from utilities.exceptions import AbortScript
import json


class heartbeat(Script):
    
    class Meta:
        name = "heartbeat"
        description = "Heartbeat"
        
    def run(self, data, commit):
        self.log_info("Heartbeat")
        
        return ("Done")
        
class quicktest2(Script):
        
    class Meta:
        name = "quicktest2"
        description = "quicktest2"
        
    def run(self, data, commit):
        self.log_info("quicktest2")
        
        return ("Done")
    
