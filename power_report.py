from dcim.models import Device, PowerPort, Site
from extras.scripts import Script, ObjectVar

class SinglePowerPortReport(Script):
    class Meta:
        name = "Single Connected Power Port Report"
        description = "Report devices at a given site that only have a single connected power port"

    site = ObjectVar(
        model=Site,
        description="Select the site to report on"
    )

    def run(self, data, commit):
        site = data["site"]
        devices_with_single_power_port = []

        # Get all devices at the selected site
        devices = Device.objects.filter(site=site)

        for device in devices:
            # Get all power ports for this device
            power_ports = PowerPort.objects.filter(device=device)
            
            # Count how many power ports are connected
            connected_power_ports = sum([1 for port in power_ports if port.connected_endpoint])

            # If there's exactly one connected power port, add the device to the list
            if connected_power_ports == 1:
                devices_with_single_power_port.append(device)

        # Output the result
        if devices_with_single_power_port:
            for device in devices_with_single_power_port:
                self.log_info(f"Device: {device.name} ({device.device_type}) has only 1 connected power port.")
        else:
            self.log_info("No devices with a single connected power port found.")

        return f"Found {len(devices_with_single_power_port)} devices with a single connected power port."
