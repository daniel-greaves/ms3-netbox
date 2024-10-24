from dcim.models import Device, PowerPort, Site
from extras.reports import Report, BooleanVar, StringVar

class SinglePowerPortReport(Report):
    """Report to check for devices with only a single power port at a user-specified site"""

    # Description of the report
    description = "Checks all devices at a specified site and flags any that have only a single power port."

    # Add a user input variable for site_slug
    site_slug = StringVar(
        description="Slug of the site to check",
        label="Site Slug"
    )

    def test_device_power_ports(self, site_slug):
        # Validate that the site exists
        try:
            site = Site.objects.get(slug=site_slug)
        except Site.DoesNotExist:
            self.log_failure(None, f"Site with slug '{site_slug}' does not exist.")
            return

        # Query all devices at the specified site
        devices = Device.objects.filter(site=site)

        # Iterate through each device
        for device in devices:
            # Count the number of power ports
            power_ports = PowerPort.objects
