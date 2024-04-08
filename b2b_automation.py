from extras.scripts import *
from django.utils.text import slugify

from dcim.choices import DeviceStatusChoices, SiteStatusChoices
from dcim.models import Device, DeviceRole, DeviceType, Site

class NewBranchScript(Script):

    class Meta:
        name = "New B2B Order"
        description = "Provision a new business connection"

    site_name = StringVar(
        description="Name of the new site"
    )
    switch_count = IntegerVar(
        description="Number of access switches to create"
    )
    switch_model = ObjectVar(
        description="Access switch model",
        model=DeviceType
    )
    router_count = IntegerVar(
        description="Number of routers to create"
    )
    router_model = ObjectVar(
        description="Router model",
        model=DeviceType
    )
    ap_count = IntegerVar(
        description="Number of APs to create"
    )
    ap_model = ObjectVar(
        description="AP model",
        model=DeviceType,
        query_params={
            'manufacturer': 'adva'
        }
    )
    ip_address = IPAddressWithMaskVar(
        description="IP Address of ADVA"
    )
    server_count = IntegerVar(
        description="Number of servers to create"
    )
    server_model = ObjectVar(
        description="Server model",
        model=DeviceType
    )
